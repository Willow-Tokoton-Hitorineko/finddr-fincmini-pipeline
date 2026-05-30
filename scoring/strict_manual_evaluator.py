"""
严格遵循DeepEval标准的人工评估器
完全模拟 SummarizationMetric 的评分逻辑
"""

import json
import re
from typing import List, Dict
from datetime import datetime


# 完全按照 evaluation_score.py 中的预定义问题
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


class StrictManualEvaluator:
    """
    严格遵循DeepEval SummarizationMetric的评估器
    
    评分逻辑（完全按照DeepEval）：
    1. Alignment Score: 检查是否有虚构、矛盾、无依据的信息（基于原文真实信息）
    2. Coverage Score: 检查是否回答了assessment_questions（基于问题覆盖）
    3. Final Score = min(Alignment Score, Coverage Score)
    """
    
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold
        self.questions = SECTION_ASSESSMENT_QUESTIONS
    
    def evaluate_section(
        self,
        section_name: str,
        original_text: str,
        generated_text: str,
        assessment_questions: List[str]
    ) -> Dict:
        """
        评估单个章节
        
        此函数返回评估框架，实际评分需要人工填入
        评估时需要：
        1. 提取原文中的关键真实信息（truths）
        2. 检查生成内容是否与真实信息对齐（alignment）
        3. 检查生成内容是否回答了评估问题（coverage）
        """
        
        print(f"\n{'='*80}")
        print(f"评估章节: {section_name}")
        print(f"{'='*80}")
        print(f"评估问题数量: {len(assessment_questions)}")
        for i, q in enumerate(assessment_questions, 1):
            print(f"  {i}. {q}")
        
        # === 这里是人工评估的接口 ===
        # AI分析师需要填入以下三个值：
        
        alignment_score = 0.0    # 对齐分数（0-1）
        coverage_score = 0.0     # 覆盖率分数（0-1）
        reason = ""              # 评估原因
        
        # === 评估框架结束 ===
        
        final_score = min(alignment_score, coverage_score)
        
        return {
            "section_name": section_name,
            "score": final_score,
            "alignment_score": alignment_score,
            "coverage_score": coverage_score,
            "reason": reason,
            "assessment_questions": assessment_questions,
            "passed": final_score >= self.threshold
        }
    
    def evaluate_full_report(
        self,
        original_report_path: str,
        generated_report_path: str,
        output_path: str = "strict_evaluation_result.json"
    ) -> Dict:
        """评估完整报告"""
        
        print("="*80)
        print("严格遵循DeepEval标准的年报评估系统")
        print("="*80)
        
        # 读取文件
        with open(original_report_path, 'r', encoding='utf-8') as f:
            original_text = f.read()
        
        with open(generated_report_path, 'r', encoding='utf-8') as f:
            generated_text = f.read()
        
        print(f"\n数据来源:")
        print(f"  - 原始年报: {original_report_path}")
        print(f"  - 生成报告: {generated_report_path}")
        print(f"\n数据统计:")
        print(f"  - 原文长度: {len(original_text):,} 字符")
        print(f"  - 报告长度: {len(generated_text):,} 字符")
        
        # 提取章节
        sections = self._extract_sections(generated_text)
        
        # 评估每个章节
        results = []
        for section_name, section_content in sections.items():
            # 获取评估问题
            section_key = self._map_section_key(section_name)
            questions = self.questions.get(section_key, [])
            
            if questions:  # 只评估有预定义问题的章节
                result = self.evaluate_section(
                    section_name=section_name,
                    original_text=original_text,
                    generated_text=section_content,
                    assessment_questions=questions
                )
                results.append(result)
        
        # 计算总体分数（与DeepEval一致）
        if results:
            overall_score = sum(r['score'] for r in results) / len(results)
            overall_alignment = sum(r['alignment_score'] for r in results) / len(results)
            overall_coverage = sum(r['coverage_score'] for r in results) / len(results)
        else:
            overall_score = overall_alignment = overall_coverage = 0.0
        
        final_result = {
            "evaluation_metadata": {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "evaluator": "Strict Manual Evaluator (DeepEval Compatible)",
                "threshold": self.threshold,
                "data_sources": {
                    "original": original_report_path,
                    "generated": generated_report_path
                }
            },
            "overall_score": round(overall_score, 4),
            "overall_alignment_score": round(overall_alignment, 4),
            "overall_coverage_score": round(overall_coverage, 4),
            "passed": overall_score >= self.threshold,
            "total_sections": len(results),
            "passed_sections": sum(1 for r in results if r['passed']),
            "section_results": results
        }
        
        # 保存结果
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(final_result, f, ensure_ascii=False, indent=2)
        
        print(f"\n{'='*80}")
        print("评估完成")
        print(f"{'='*80}")
        print(f"总体分数: {final_result['overall_score']:.3f}")
        print(f"对齐分数: {final_result['overall_alignment_score']:.3f}")
        print(f"覆盖率分数: {final_result['overall_coverage_score']:.3f}")
        print(f"通过状态: {'✓ 通过' if final_result['passed'] else '✗ 未通过'}")
        print(f"结果已保存: {output_path}")
        
        return final_result
    
    def _extract_sections(self, text: str) -> Dict[str, str]:
        """提取章节"""
        sections = {}
        pattern = r'#\s+(Section\s+\d+(?:\.\d+)?[:\s]+[^\n]+)'
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        
        for i, match in enumerate(matches):
            section_title = match.group(1).strip()
            start_pos = match.end()
            end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            section_content = text[start_pos:end_pos].strip()
            sections[section_title] = section_content
        
        return sections
    
    def _map_section_key(self, section_name: str) -> str:
        """映射章节名到评估问题的key"""
        # Section 3.1 Profitability Analysis -> Section 3.1 Profitability Analysis
        match = re.search(r'Section\s+(\d+\.\d+)', section_name, re.IGNORECASE)
        if match:
            section_num = match.group(1)
            for key in self.questions.keys():
                if key.startswith(f"Section {section_num}"):
                    return key
        return section_name


def main():
    """使用示例"""
    evaluator = StrictManualEvaluator(threshold=0.5)
    
    # 评估报告
    result = evaluator.evaluate_full_report(
        original_report_path="../中国移动/中国移动2024年年报.md",
        generated_report_path="../600941_Analysis(4).md",
        output_path="strict_evaluation_result.json"
    )


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) >= 3:
        original = sys.argv[1]
        generated = sys.argv[2]
        threshold = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
        
        evaluator = StrictManualEvaluator(threshold=threshold)
        evaluator.evaluate_full_report(original, generated)
    else:
        main()

