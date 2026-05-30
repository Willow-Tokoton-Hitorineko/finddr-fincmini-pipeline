"""
AI人工评估脚本 - 无需API调用
保持与DeepEval相同的评分逻辑：
- 对齐分数 (Alignment Score): 检查虚构/矛盾信息
- 覆盖率分数 (Coverage Score): 检查关键信息覆盖
- 最终分数 = min(对齐分数, 覆盖率分数)
"""

import json
import re
from typing import List, Dict, Tuple
from datetime import datetime


class ManualEvaluator:
    """手动评估器 - 模拟DeepEval逻辑但由AI分析师执行"""
    
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold
        self.evaluation_questions = {
            "Section 1.1": [
                "是否准确列出了公司名称?",
                "成立日期是否正确?",
                "总部地址是否完整准确?"
            ],
            "Section 1.2": [
                "是否准确描述了创新优势?",
                "产品优势描述是否基于原文?",
                "品牌认知度数据是否准确?",
                "声誉评级是否有原文依据?"
            ],
            "Section 1.3": [
                "使命陈述是否准确?",
                "愿景陈述是否正确?",
                "核心价值观是否如实反映?"
            ],
            "Section 2.1": [
                "收入数据是否准确?",
                "成本数据是否正确?",
                "利润数据是否无误?",
                "所有财务数字是否与原文一致?"
            ],
            "Section 2.2": [
                "资产数据是否准确?",
                "负债数据是否正确?",
                "权益数据是否无误?",
                "所有资产负债表项目是否完整?"
            ],
            "Section 2.3": [
                "经营现金流数据是否准确?",
                "投资现金流数据是否正确?",
                "融资现金流数据是否无误?",
                "股利数据是否准确?"
            ],
            "Section 2.4": [
                "毛利率计算是否正确?",
                "营业利润率是否准确?",
                "所有财务比率是否正确计算?"
            ],
            "Section 2.5": [
                "产品/服务收入分类是否完整?",
                "地区收入数据是否准确?"
            ],
            "Section 3.1": [
                "是否包含收入增长率的讨论?",
                "是否准确反映了毛利率的变化趋势?",
                "是否提及了营业利润率的表现?",
                "是否讨论了有效税率的影响?",
                "是否分析了非经常性项目的影响?"
            ],
            "Section 3.2": [
                "是否全面评估了公司的财务健康状况?",
                "是否分析了盈利能力和收益质量?",
                "是否评估了运营效率?",
                "是否识别了主要财务风险?",
                "是否对未来财务表现做出了预测?"
            ],
            "Section 3.3": [
                "是否清晰描述了公司的商业模式?",
                "是否准确评估了公司的市场地位?",
                "是否提供了市场份额的相关信息?"
            ],
            "Section 4.1": [
                "是否识别了主要的市场风险?",
                "是否讨论了运营风险?",
                "是否分析了财务风险?",
                "是否涵盖了合规风险?"
            ],
            "Section 5.1": [
                "是否准确列出了董事会成员姓名?",
                "是否正确标注了职位?",
                "是否包含了薪酬信息?"
            ],
            "Section 5.2": [
                "是否描述了风险评估程序?",
                "是否说明了控制活动?",
                "是否介绍了监督机制?",
                "是否披露了内部控制的有效性?",
                "是否识别了重大缺陷或不足?"
            ],
            "Section 6.1": [
                "是否讨论了并购战略?",
                "是否介绍了新技术方向?",
                "是否提及组织重组计划?"
            ],
            "Section 6.2": [
                "是否分析了经济挑战?",
                "是否讨论了竞争压力?"
            ],
            "Section 6.3": [
                "是否说明了研发投入情况?",
                "是否介绍了新产品发布计划?"
            ]
        }
    
    def evaluate_report(
        self,
        original_report_path: str,
        generated_report_path: str
    ) -> Dict:
        """
        评估完整报告
        
        Returns:
            评估结果字典
        """
        print("=" * 80)
        print("年报分析质量评估系统 - AI人工评估版")
        print("=" * 80)
        
        # 读取文件
        print(f"\n正在读取原始年报: {original_report_path}")
        with open(original_report_path, 'r', encoding='utf-8') as f:
            original_text = f.read()
        
        print(f"正在读取生成报告: {generated_report_path}")
        with open(generated_report_path, 'r', encoding='utf-8') as f:
            generated_text = f.read()
        
        print(f"\n原始年报长度: {len(original_text):,} 字符")
        print(f"生成报告长度: {len(generated_text):,} 字符")
        
        # 提取章节
        sections = self._extract_sections(generated_text)
        print(f"\n检测到 {len(sections)} 个章节")
        
        # 评估每个章节
        section_results = []
        print("\n" + "=" * 80)
        print("开始逐章节评估")
        print("=" * 80)
        
        for section_name, section_content in sections.items():
            print(f"\n>>> 评估章节: {section_name}")
            result = self._evaluate_section(
                section_name=section_name,
                section_content=section_content,
                original_text=original_text
            )
            section_results.append(result)
            print(f"    分数: {result['score']:.3f} | 对齐: {result['alignment_score']:.3f} | 覆盖: {result['coverage_score']:.3f}")
        
        # 计算总体分数
        overall_score = sum(r['score'] for r in section_results) / len(section_results) if section_results else 0
        overall_alignment = sum(r['alignment_score'] for r in section_results) / len(section_results) if section_results else 0
        overall_coverage = sum(r['coverage_score'] for r in section_results) / len(section_results) if section_results else 0
        
        final_result = {
            "evaluation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "evaluator": "AI Manual Evaluator (Claude)",
            "overall_score": round(overall_score, 4),
            "overall_alignment_score": round(overall_alignment, 4),
            "overall_coverage_score": round(overall_coverage, 4),
            "passed": overall_score >= self.threshold,
            "threshold": self.threshold,
            "total_sections": len(section_results),
            "passed_sections": sum(1 for r in section_results if r['score'] >= self.threshold),
            "section_results": section_results,
            "original_file": original_report_path,
            "generated_file": generated_report_path
        }
        
        # 显示总体结果
        self._print_summary(final_result)
        
        return final_result
    
    def _extract_sections(self, text: str) -> Dict[str, str]:
        """提取报告中的各个章节"""
        sections = {}
        
        # 匹配 Section X 或 Section X.Y 格式
        pattern = r'#\s+(Section\s+\d+(?:\.\d+)?[:\s]+[^\n]+)'
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        
        for i, match in enumerate(matches):
            section_title = match.group(1).strip()
            start_pos = match.end()
            end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            section_content = text[start_pos:end_pos].strip()
            sections[section_title] = section_content
        
        return sections
    
    def _evaluate_section(
        self,
        section_name: str,
        section_content: str,
        original_text: str
    ) -> Dict:
        """
        评估单个章节
        这里使用固定的评分逻辑 - 实际评估需要AI分析师手动执行
        
        评分标准：
        1. 对齐分数: 检查是否有虚构、矛盾或无依据的信息
        2. 覆盖率分数: 检查是否覆盖了原文的关键信息
        3. 最终分数 = min(对齐分数, 覆盖率分数)
        """
        
        # 这里是占位符 - 实际评分需要人工分析
        # 在真实应用中，AI分析师会在这里手动填入评分
        
        # 获取该章节的评估问题
        section_key = self._get_section_key(section_name)
        questions = self.evaluation_questions.get(section_key, [])
        
        # 初始化评分（需要手动填入）
        alignment_score = 0.0  # 待填入
        coverage_score = 0.0   # 待填入
        reason = f"需要对 {section_name} 进行人工评估"
        
        # 根据章节特征设置默认分数（这是占位符）
        # 实际应用中这些分数由AI分析师通过详细对比得出
        
        return {
            "section_name": section_name,
            "score": min(alignment_score, coverage_score),
            "alignment_score": alignment_score,
            "coverage_score": coverage_score,
            "reason": reason,
            "questions_used": questions,
            "content_length": len(section_content)
        }
    
    def _get_section_key(self, section_name: str) -> str:
        """从完整章节名提取章节编号"""
        match = re.search(r'Section\s+(\d+(?:\.\d+)?)', section_name, re.IGNORECASE)
        if match:
            return f"Section {match.group(1)}"
        return section_name
    
    def _print_summary(self, result: Dict):
        """打印评估摘要"""
        print("\n" + "=" * 80)
        print("评估结果汇总")
        print("=" * 80)
        print(f"\n总体分数: {result['overall_score']:.3f}")
        print(f"  - 对齐分数: {result['overall_alignment_score']:.3f}")
        print(f"  - 覆盖率分数: {result['overall_coverage_score']:.3f}")
        print(f"\n是否通过: {'✓ 是' if result['passed'] else '✗ 否'} (阈值: {result['threshold']})")
        print(f"通过章节: {result['passed_sections']}/{result['total_sections']}")
        print("=" * 80)


def save_evaluation_result(result: Dict, output_path: str = "ai_evaluation_result.json"):
    """保存评估结果"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n✓ 评估结果已保存至: {output_path}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) >= 3:
        original = sys.argv[1]
        generated = sys.argv[2]
        threshold = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
        
        evaluator = ManualEvaluator(threshold=threshold)
        result = evaluator.evaluate_report(original, generated)
        save_evaluation_result(result)
    else:
        print("使用方法: python ai_manual_evaluate.py <原始年报> <生成报告> [阈值]")
        print("示例: python ai_manual_evaluate.py ../中国移动/中国移动2024年年报.md 600941_Analysis(4).md 0.5")

