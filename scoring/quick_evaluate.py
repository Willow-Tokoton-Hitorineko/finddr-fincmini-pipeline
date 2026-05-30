"""
快速评估脚本
用于快速评估年报分析的质量
"""

from deepeval.test_case import LLMTestCase
from deepeval.metrics import SummarizationMetric
import json
import os


def quick_evaluate(
    original_report_path: str,
    generated_report_path: str,
    model: str = "gpt-4",
    threshold: float = 0.5,
    output_path: str = "quick_evaluation_result.json"
):
    """
    快速评估函数
    
    Args:
        original_report_path: 原始年报文件路径
        generated_report_path: 生成的分析报告文件路径
        model: 评估模型
        threshold: 通过阈值
        output_path: 结果输出路径
    """
    
    print("=" * 60)
    print("年报分析质量快速评估")
    print("=" * 60)
    
    # 读取文件
    print(f"\n读取原始年报: {original_report_path}")
    with open(original_report_path, 'r', encoding='utf-8') as f:
        original_text = f.read()
    
    print(f"读取生成报告: {generated_report_path}")
    with open(generated_report_path, 'r', encoding='utf-8') as f:
        generated_text = f.read()
    
    print(f"\n原始年报长度: {len(original_text)} 字符")
    print(f"生成报告长度: {len(generated_text)} 字符")
    
    # 创建测试用例
    test_case = LLMTestCase(
        input=original_text,
        actual_output=generated_text
    )
    
    # 创建评估指标（自动生成评估问题）
    print(f"\n使用模型: {model}")
    print(f"通过阈值: {threshold}")
    print("\n开始评估...")
    
    metric = SummarizationMetric(
        threshold=threshold,
        model=model,
        n=10,  # 自动生成10个评估问题
        include_reason=True,
        strict_mode=False,
        async_mode=True,
        verbose_mode=False
    )
    
    # 执行评估
    metric.measure(test_case)
    
    # 整理结果
    result = {
        "overall_score": metric.score,
        "passed": metric.score >= threshold,
        "threshold": threshold,
        "score_breakdown": {
            "alignment_score": metric.score_breakdown.get("Alignment Score", 0),
            "coverage_score": metric.score_breakdown.get("Coverage Score", 0)
        },
        "reason": metric.reason,
        "model_used": model,
        "original_length": len(original_text),
        "generated_length": len(generated_text)
    }
    
    # 显示结果
    print("\n" + "=" * 60)
    print("评估结果")
    print("=" * 60)
    print(f"\n✓ 总体分数: {result['overall_score']:.3f}")
    print(f"  - 对齐分数 (Alignment): {result['score_breakdown']['alignment_score']:.3f}")
    print(f"  - 覆盖率分数 (Coverage): {result['score_breakdown']['coverage_score']:.3f}")
    print(f"\n✓ 是否通过: {'是' if result['passed'] else '否'} (阈值: {threshold})")
    print(f"\n✓ 评估原因:")
    print(f"  {result['reason']}")
    
    # 保存结果
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ 结果已保存至: {output_path}")
    print("=" * 60)
    
    return result


def evaluate_with_custom_questions(
    original_report_path: str,
    generated_report_path: str,
    assessment_questions: list,
    model: str = "gpt-4",
    threshold: float = 0.5,
    output_path: str = "custom_evaluation_result.json"
):
    """
    使用自定义问题评估
    
    Args:
        original_report_path: 原始年报文件路径
        generated_report_path: 生成的分析报告文件路径
        assessment_questions: 评估问题列表
        model: 评估模型
        threshold: 通过阈值
        output_path: 结果输出路径
    """
    
    print("=" * 60)
    print("年报分析质量评估（自定义问题）")
    print("=" * 60)
    
    # 读取文件
    with open(original_report_path, 'r', encoding='utf-8') as f:
        original_text = f.read()
    
    with open(generated_report_path, 'r', encoding='utf-8') as f:
        generated_text = f.read()
    
    print(f"\n评估问题数量: {len(assessment_questions)}")
    print("评估问题:")
    for i, q in enumerate(assessment_questions, 1):
        print(f"  {i}. {q}")
    
    # 创建测试用例
    test_case = LLMTestCase(
        input=original_text,
        actual_output=generated_text
    )
    
    # 创建评估指标
    print(f"\n使用模型: {model}")
    print("\n开始评估...")
    
    metric = SummarizationMetric(
        threshold=threshold,
        model=model,
        assessment_questions=assessment_questions,
        include_reason=True,
        strict_mode=False,
        async_mode=True,
        verbose_mode=False
    )
    
    # 执行评估
    metric.measure(test_case)
    
    # 整理结果
    result = {
        "overall_score": metric.score,
        "passed": metric.score >= threshold,
        "threshold": threshold,
        "score_breakdown": {
            "alignment_score": metric.score_breakdown.get("Alignment Score", 0),
            "coverage_score": metric.score_breakdown.get("Coverage Score", 0)
        },
        "reason": metric.reason,
        "assessment_questions": assessment_questions,
        "model_used": model
    }
    
    # 显示结果
    print("\n" + "=" * 60)
    print("评估结果")
    print("=" * 60)
    print(f"\n✓ 总体分数: {result['overall_score']:.3f}")
    print(f"  - 对齐分数: {result['score_breakdown']['alignment_score']:.3f}")
    print(f"  - 覆盖率分数: {result['score_breakdown']['coverage_score']:.3f}")
    print(f"\n✓ 是否通过: {'是' if result['passed'] else '否'}")
    print(f"\n✓ 评估原因:")
    print(f"  {result['reason']}")
    
    # 保存结果
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ 结果已保存至: {output_path}")
    print("=" * 60)
    
    return result


def main():
    """主函数"""
    
    # 示例1: 快速评估（自动生成评估问题）
    print("\n示例1: 快速评估（自动生成评估问题）")
    print("-" * 60)
    
    # 请根据实际文件路径修改
    original_report = "../中国移动2024年年报.md"
    generated_report = "600941_Analysis(2).md"
    
    if os.path.exists(original_report) and os.path.exists(generated_report):
        result1 = quick_evaluate(
            original_report_path=original_report,
            generated_report_path=generated_report,
            model="gpt-4",
            threshold=0.5,
            output_path="quick_result.json"
        )
    else:
        print(f"文件不存在，请检查路径:")
        print(f"  - 原始年报: {original_report}")
        print(f"  - 生成报告: {generated_report}")
    
    # 示例2: 使用自定义问题评估
    print("\n\n示例2: 使用自定义问题评估")
    print("-" * 60)
    
    custom_questions = [
        "分析是否包含2023-2024年的收入增长率?",
        "是否准确反映了毛利率从27.78%到29.01%的变化?",
        "是否讨论了CHBN业务结构的发展?",
        "是否提及数字化转型收入占比提升至31.3%?",
        "是否分析了政企市场和新兴市场的增长情况?",
        "是否讨论了EBITDA占主营业务收入比的表现?",
        "是否准确反映了有效税率的稳定性?",
        "是否分析了非经常性损益对盈利质量的影响?",
        "是否识别了主要的财务风险因素?",
        "是否对未来财务表现做出了合理预测?"
    ]
    
    if os.path.exists(original_report) and os.path.exists(generated_report):
        result2 = evaluate_with_custom_questions(
            original_report_path=original_report,
            generated_report_path=generated_report,
            assessment_questions=custom_questions,
            model="gpt-4",
            threshold=0.5,
            output_path="custom_result.json"
        )
    else:
        print("请先设置正确的文件路径")


if __name__ == "__main__":
    import sys
    
    # 命令行使用示例
    if len(sys.argv) >= 3:
        # python quick_evaluate.py <原始年报> <生成报告> [模型] [阈值]
        original = sys.argv[1]
        generated = sys.argv[2]
        model = sys.argv[3] if len(sys.argv) > 3 else "gpt-4"
        threshold = float(sys.argv[4]) if len(sys.argv) > 4 else 0.5
        
        quick_evaluate(
            original_report_path=original,
            generated_report_path=generated,
            model=model,
            threshold=threshold
        )
    else:
        # 运行示例
        main()

