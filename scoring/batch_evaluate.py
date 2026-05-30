"""
批量评估脚本
用于批量评估多个报告或多个章节
"""

from evaluation_score import AnnualReportEvaluator, SECTION_ASSESSMENT_QUESTIONS
import pandas as pd
import json
import os
from pathlib import Path
from typing import List, Dict
import re


def extract_section_content(markdown_text: str, section_name: str) -> str:
    """
    从Markdown文本中提取特定章节的内容
    
    Args:
        markdown_text: Markdown格式的文本
        section_name: 章节名称，如 "Section 3.1"
        
    Returns:
        章节内容
    """
    # 构建章节标题的正则表达式
    # 支持 "# Section 3.1" 或 "## S3.1" 等格式
    pattern = rf'#+\s*(?:S|Section)\s*{re.escape(section_name.split()[-1])}\s*[:\-]?\s*.*?\n(.*?)(?=#+\s*(?:S|Section)\s*\d+\.\d+|$)'
    
    match = re.search(pattern, markdown_text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    # 如果没找到，尝试更宽松的匹配
    pattern2 = rf'#+\s*.*?{re.escape(section_name)}.*?\n(.*?)(?=#+\s*Section|#+\s*S\d|$)'
    match = re.search(pattern2, markdown_text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    
    return ""


def load_sections_from_files(
    original_report_path: str,
    generated_report_path: str,
    sections_to_evaluate: List[str] = None
) -> List[Dict]:
    """
    从文件中加载章节数据
    
    Args:
        original_report_path: 原始年报文件路径
        generated_report_path: 生成的分析报告文件路径
        sections_to_evaluate: 要评估的章节列表（可选）
        
    Returns:
        章节数据列表
    """
    # 读取文件
    with open(original_report_path, 'r', encoding='utf-8') as f:
        original_text = f.read()
    
    with open(generated_report_path, 'r', encoding='utf-8') as f:
        generated_text = f.read()
    
    # 默认评估所有章节
    if sections_to_evaluate is None:
        sections_to_evaluate = list(SECTION_ASSESSMENT_QUESTIONS.keys())
    
    sections_data = []
    
    for section_name in sections_to_evaluate:
        # 提取章节内容
        section_id = section_name.split()[0] + " " + section_name.split()[1]  # 如 "Section 3.1"
        
        # 对于原始年报，可能需要提取对应的内容
        # 这里简化处理，使用完整的原始文本
        original_section = original_text
        
        # 从生成的报告中提取对应章节
        generated_section = extract_section_content(generated_text, section_id)
        
        if not generated_section:
            print(f"警告: 未找到章节 {section_name} 的内容")
            continue
        
        sections_data.append({
            "section_name": section_name,
            "original_text": original_section,
            "generated_summary": generated_section,
            "assessment_questions": SECTION_ASSESSMENT_QUESTIONS.get(section_name)
        })
    
    return sections_data


def batch_evaluate_reports(
    report_pairs: List[Dict],
    model: str = "gpt-4",
    threshold: float = 0.5,
    output_dir: str = "batch_results"
):
    """
    批量评估多个报告
    
    Args:
        report_pairs: 报告对列表，每个元素包含:
            - name: 报告名称
            - original: 原始年报路径
            - generated: 生成报告路径
        model: 评估模型
        threshold: 通过阈值
        output_dir: 输出目录
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 初始化评估器
    evaluator = AnnualReportEvaluator(model=model, threshold=threshold)
    
    all_results = []
    
    print("=" * 80)
    print(f"批量评估 {len(report_pairs)} 个报告")
    print("=" * 80)
    
    for i, pair in enumerate(report_pairs, 1):
        print(f"\n[{i}/{len(report_pairs)}] 评估报告: {pair['name']}")
        print("-" * 80)
        
        try:
            # 加载章节数据
            sections_data = load_sections_from_files(
                original_report_path=pair['original'],
                generated_report_path=pair['generated']
            )
            
            # 评估完整报告
            output_file = os.path.join(output_dir, f"{pair['name']}_evaluation.json")
            result = evaluator.evaluate_full_report(
                sections_data=sections_data,
                output_file=output_file
            )
            
            # 添加报告名称
            result['report_name'] = pair['name']
            result['original_path'] = pair['original']
            result['generated_path'] = pair['generated']
            
            all_results.append(result)
            
        except Exception as e:
            print(f"错误: 评估 {pair['name']} 时出错: {str(e)}")
            continue
    
    # 生成汇总报告
    summary_df = pd.DataFrame([{
        '报告名称': r['report_name'],
        '整体分数': r['overall_score'],
        '对齐分数': r['overall_alignment_score'],
        '覆盖率分数': r['overall_coverage_score'],
        '总章节数': r['total_sections'],
        '通过章节数': r['passed_sections'],
        '通过率': f"{r['passed_sections']/r['total_sections']*100:.1f}%"
    } for r in all_results])
    
    # 保存汇总结果
    summary_file = os.path.join(output_dir, "summary.csv")
    summary_df.to_csv(summary_file, index=False, encoding='utf-8-sig')
    
    summary_json = os.path.join(output_dir, "summary.json")
    with open(summary_json, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    # 打印汇总
    print("\n" + "=" * 80)
    print("批量评估汇总")
    print("=" * 80)
    print(summary_df.to_string(index=False))
    print(f"\n详细结果已保存至: {output_dir}")
    print(f"  - 汇总表格: {summary_file}")
    print(f"  - 汇总JSON: {summary_json}")
    print("=" * 80)
    
    return all_results


def evaluate_single_report_all_sections(
    original_report_path: str,
    generated_report_path: str,
    report_name: str = "report",
    model: str = "gpt-4",
    threshold: float = 0.5,
    output_dir: str = "section_results"
):
    """
    评估单个报告的所有章节
    
    Args:
        original_report_path: 原始年报路径
        generated_report_path: 生成报告路径
        report_name: 报告名称
        model: 评估模型
        threshold: 通过阈值
        output_dir: 输出目录
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 初始化评估器
    evaluator = AnnualReportEvaluator(model=model, threshold=threshold)
    
    print("=" * 80)
    print(f"评估报告所有章节: {report_name}")
    print("=" * 80)
    
    # 加载章节数据
    print("\n加载章节数据...")
    sections_data = load_sections_from_files(
        original_report_path=original_report_path,
        generated_report_path=generated_report_path
    )
    
    print(f"找到 {len(sections_data)} 个章节")
    
    # 评估完整报告
    output_file = os.path.join(output_dir, f"{report_name}_full_evaluation.json")
    result = evaluator.evaluate_full_report(
        sections_data=sections_data,
        output_file=output_file
    )
    
    # 生成章节详细表格
    sections_df = pd.DataFrame([{
        '章节': r['section_name'].split(':', 1)[0],
        '总分': f"{r['score']:.3f}",
        '对齐分数': f"{r['alignment_score']:.3f}",
        '覆盖率分数': f"{r['coverage_score']:.3f}",
        '是否通过': '✓' if r['score'] >= threshold else '✗'
    } for r in result['section_results']])
    
    # 保存章节详细结果
    sections_file = os.path.join(output_dir, f"{report_name}_sections.csv")
    sections_df.to_csv(sections_file, index=False, encoding='utf-8-sig')
    
    # 打印结果
    print("\n" + "=" * 80)
    print("章节评估详情")
    print("=" * 80)
    print(sections_df.to_string(index=False))
    print("\n" + "=" * 80)
    print("总体评估")
    print("=" * 80)
    print(f"整体分数: {result['overall_score']:.3f}")
    print(f"对齐分数: {result['overall_alignment_score']:.3f}")
    print(f"覆盖率分数: {result['overall_coverage_score']:.3f}")
    print(f"通过章节: {result['passed_sections']}/{result['total_sections']}")
    print(f"通过率: {result['passed_sections']/result['total_sections']*100:.1f}%")
    print("=" * 80)
    print(f"\n结果已保存至: {output_dir}")
    print(f"  - 完整结果: {output_file}")
    print(f"  - 章节详情: {sections_file}")
    
    return result


def main():
    """主函数示例"""
    
    # 示例1: 评估单个报告的所有章节
    print("\n示例1: 评估单个报告的所有章节")
    print("=" * 80)
    
    original_report = "../中国移动2024年年报.md"
    generated_report = "600941_Analysis(2).md"
    
    if os.path.exists(original_report) and os.path.exists(generated_report):
        result1 = evaluate_single_report_all_sections(
            original_report_path=original_report,
            generated_report_path=generated_report,
            report_name="中国移动2024",
            model="gpt-4",
            threshold=0.5,
            output_dir="section_eval_results"
        )
    else:
        print("文件不存在，跳过示例1")
    
    # 示例2: 批量评估多个报告
    print("\n\n示例2: 批量评估多个报告")
    print("=" * 80)
    
    report_pairs = [
        {
            "name": "中国移动2024",
            "original": "../中国移动2024年年报.md",
            "generated": "600941_Analysis(2).md"
        },
        # 可以添加更多报告...
        # {
        #     "name": "中国移动2023",
        #     "original": "../中国移动2023年年报.md",
        #     "generated": "600941_Analysis_2023.md"
        # },
    ]
    
    # 过滤存在的文件
    valid_pairs = [p for p in report_pairs 
                   if os.path.exists(p['original']) and os.path.exists(p['generated'])]
    
    if valid_pairs:
        result2 = batch_evaluate_reports(
            report_pairs=valid_pairs,
            model="gpt-4",
            threshold=0.5,
            output_dir="batch_eval_results"
        )
    else:
        print("没有找到有效的报告文件对，跳过示例2")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) >= 3:
        # 命令行使用: python batch_evaluate.py <原始年报> <生成报告> [报告名称]
        original = sys.argv[1]
        generated = sys.argv[2]
        name = sys.argv[3] if len(sys.argv) > 3 else "report"
        
        evaluate_single_report_all_sections(
            original_report_path=original,
            generated_report_path=generated,
            report_name=name
        )
    else:
        # 运行示例
        main()

