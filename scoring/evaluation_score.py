"""
年报分析质量评分系统
基于 DeepEval SummarizationMetric 实现
"""

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import SummarizationMetric
from deepeval.dataset import Golden
import pandas as pd
from typing import List, Dict
import json


class AnnualReportEvaluator:
    """年报分析评分器"""
    
    def __init__(self, model="gpt-4", threshold=0.5):
        """
        初始化评分器
        
        Args:
            model: 使用的评估模型，默认 gpt-4
            threshold: 通过阈值，默认 0.5
        """
        self.model = model
        self.threshold = threshold
        
    def create_section_metric(
        self, 
        section_name: str,
        assessment_questions: List[str] = None,
        n: int = 5,
        truths_extraction_limit: int = None
    ) -> SummarizationMetric:
        """
        为特定章节创建评估指标
        
        Args:
            section_name: 章节名称
            assessment_questions: 评估问题列表（可选）
            n: 自动生成问题数量
            truths_extraction_limit: 真实信息提取限制
        """
        return SummarizationMetric(
            threshold=self.threshold,
            model=self.model,
            assessment_questions=assessment_questions,
            n=n,
            include_reason=True,
            strict_mode=False,
            async_mode=True,
            verbose_mode=False,
            truths_extraction_limit=truths_extraction_limit
        )
    
    def evaluate_section(
        self,
        original_text: str,
        generated_summary: str,
        section_name: str,
        assessment_questions: List[str] = None
    ) -> Dict:
        """
        评估单个章节
        
        Args:
            original_text: 原始年报文本
            generated_summary: 生成的分析内容
            section_name: 章节名称
            assessment_questions: 评估问题（可选）
            
        Returns:
            包含分数、原因和详细分解的字典
        """
        # 创建测试用例
        test_case = LLMTestCase(
            input=original_text,
            actual_output=generated_summary
        )
        
        # 创建评估指标
        metric = self.create_section_metric(
            section_name=section_name,
            assessment_questions=assessment_questions
        )
        
        # 执行评估
        metric.measure(test_case)
        
        return {
            "section_name": section_name,
            "score": metric.score,
            "reason": metric.reason,
            "score_breakdown": metric.score_breakdown,
            "alignment_score": metric.score_breakdown.get("Alignment Score", 0),
            "coverage_score": metric.score_breakdown.get("Coverage Score", 0)
        }
    
    def evaluate_full_report(
        self,
        sections_data: List[Dict],
        output_file: str = "evaluation_results.json"
    ) -> Dict:
        """
        评估完整报告的所有章节
        
        Args:
            sections_data: 章节数据列表，每个元素包含:
                - section_name: 章节名称
                - original_text: 原始年报文本
                - generated_summary: 生成的分析内容
                - assessment_questions: 评估问题（可选）
            output_file: 结果输出文件
            
        Returns:
            完整评估结果
        """
        results = []
        
        for section in sections_data:
            print(f"\n评估章节: {section['section_name']}")
            result = self.evaluate_section(
                original_text=section['original_text'],
                generated_summary=section['generated_summary'],
                section_name=section['section_name'],
                assessment_questions=section.get('assessment_questions')
            )
            results.append(result)
            print(f"分数: {result['score']:.3f}")
            print(f"对齐分数: {result['alignment_score']:.3f}")
            print(f"覆盖率分数: {result['coverage_score']:.3f}")
        
        # 计算总体分数
        overall_score = sum(r['score'] for r in results) / len(results)
        overall_alignment = sum(r['alignment_score'] for r in results) / len(results)
        overall_coverage = sum(r['coverage_score'] for r in results) / len(results)
        
        final_results = {
            "overall_score": overall_score,
            "overall_alignment_score": overall_alignment,
            "overall_coverage_score": overall_coverage,
            "section_results": results,
            "total_sections": len(results),
            "passed_sections": sum(1 for r in results if r['score'] >= self.threshold)
        }
        
        # 保存结果
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(final_results, f, ensure_ascii=False, indent=2)
        
        print(f"\n总体评估结果:")
        print(f"整体分数: {overall_score:.3f}")
        print(f"整体对齐分数: {overall_alignment:.3f}")
        print(f"整体覆盖率分数: {overall_coverage:.3f}")
        print(f"通过章节: {final_results['passed_sections']}/{final_results['total_sections']}")
        
        return final_results


# 预定义各章节的评估问题
SECTION_ASSESSMENT_QUESTIONS = {
    "Section 3.1 Profitability Analysis": [
        "分析是否包含收入增长率的讨论?",
        "是否准确反映了毛利率的变化趋势?",
        "是否提及了营业利润率的表现?",
        "是否讨论了有效税率的影响?",
        "是否分析了非经常性项目的影响?"
    ],
    "Section 3.2 Financial Performance Summary": [
        "是否全面评估了公司的财务健康状况?",
        "是否分析了盈利能力和收益质量?",
        "是否评估了运营效率?",
        "是否识别了主要财务风险?",
        "是否对未来财务表现做出了预测?"
    ],
    "Section 3.3 Business Competitiveness": [
        "是否清晰描述了公司的商业模式?",
        "是否准确评估了公司的市场地位?",
        "是否提供了市场份额的相关信息?"
    ],
    "Section 4.1 Risk Factors": [
        "是否识别了主要的市场风险?",
        "是否讨论了运营风险?",
        "是否分析了财务风险?",
        "是否涵盖了合规风险?"
    ],
    "Section 5.1 Board Composition": [
        "是否准确列出了董事会成员姓名?",
        "是否正确标注了职位?",
        "是否包含了薪酬信息?"
    ],
    "Section 5.2 Internal Controls": [
        "是否描述了风险评估程序?",
        "是否说明了控制活动?",
        "是否介绍了监督机制?",
        "是否披露了内部控制的有效性?",
        "是否识别了重大缺陷或不足?"
    ],
    "Section 6.1 Strategic Direction": [
        "是否讨论了并购战略?",
        "是否介绍了新技术方向?",
        "是否提及组织重组计划?"
    ],
    "Section 6.2 Challenges and Uncertainties": [
        "是否分析了经济挑战?",
        "是否讨论了竞争压力?"
    ],
    "Section 6.3 Innovation and Development Plans": [
        "是否说明了研发投入情况?",
        "是否介绍了新产品发布计划?"
    ]
}


def load_report_sections(report_file: str, original_report_file: str) -> List[Dict]:
    """
    从文件加载报告章节数据
    
    Args:
        report_file: 生成的分析报告文件路径
        original_report_file: 原始年报文件路径
        
    Returns:
        章节数据列表
    """
    sections_data = []
    
    # 这里需要根据实际文件格式进行解析
    # 示例实现
    with open(report_file, 'r', encoding='utf-8') as f:
        generated_content = f.read()
    
    with open(original_report_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # 按章节分割（需要根据实际格式调整）
    sections = [
        "Section 3.1",
        "Section 3.2", 
        "Section 3.3",
        "Section 4.1",
        "Section 5.1",
        "Section 5.2",
        "Section 6.1",
        "Section 6.2",
        "Section 6.3"
    ]
    
    for section in sections:
        # 提取章节内容（需要根据实际格式实现）
        section_data = {
            "section_name": section,
            "original_text": original_content,  # 实际应该提取对应章节
            "generated_summary": generated_content,  # 实际应该提取对应章节
            "assessment_questions": SECTION_ASSESSMENT_QUESTIONS.get(section)
        }
        sections_data.append(section_data)
    
    return sections_data


def main():
    """主函数示例"""
    
    # 初始化评估器
    evaluator = AnnualReportEvaluator(
        model="gpt-4",  # 可以改为 "gpt-4o" 或其他模型
        threshold=0.5
    )
    
    # 示例：评估单个章节
    print("=" * 50)
    print("示例1: 评估单个章节")
    print("=" * 50)
    
    original_text = """
    公司收入在2022-2023年间实现强劲增长7.7%，2023-2024年间继续保持稳健增长3.1%。
    毛利率持续改善，从2022年的27.78%提升至2024年的29.01%。
    数字化转型收入达到2,788亿元，占主营业务收入比提升至31.3%。
    政企市场收入增长8.8%，新兴市场收入增长8.7%。
    """
    
    generated_summary = """
    公司收入保持稳健增长，毛利率持续改善，显示出良好的成本控制能力。
    数字化转型成效显著，政企市场和新兴市场成为新的增长动力。
    """
    
    result = evaluator.evaluate_section(
        original_text=original_text,
        generated_summary=generated_summary,
        section_name="Section 3.1 Profitability Analysis",
        assessment_questions=SECTION_ASSESSMENT_QUESTIONS["Section 3.1 Profitability Analysis"]
    )
    
    print(f"\n评估结果:")
    print(f"分数: {result['score']:.3f}")
    print(f"对齐分数: {result['alignment_score']:.3f}")
    print(f"覆盖率分数: {result['coverage_score']:.3f}")
    print(f"原因: {result['reason']}")
    
    # 示例：评估完整报告
    print("\n" + "=" * 50)
    print("示例2: 评估完整报告")
    print("=" * 50)
    
    # 准备章节数据
    sections_data = [
        {
            "section_name": "Section 3.1 Profitability Analysis",
            "original_text": original_text,
            "generated_summary": generated_summary,
            "assessment_questions": SECTION_ASSESSMENT_QUESTIONS["Section 3.1 Profitability Analysis"]
        }
        # 可以添加更多章节...
    ]
    
    # 评估完整报告
    final_results = evaluator.evaluate_full_report(
        sections_data=sections_data,
        output_file="evaluation_results.json"
    )
    
    print(f"\n评估完成! 结果已保存到 evaluation_results.json")


if __name__ == "__main__":
    main()

