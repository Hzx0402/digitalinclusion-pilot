# 李克特量表信度检验（两个独立量表）
# 量表1：数字障碍量表（3题）
# 量表2：数字能力量表（4题）

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

# ============================================================
# 生成模拟数据（正式研究替换为真实问卷数据）
# ============================================================

np.random.seed(42)
n = 200

# 量表1：数字障碍（得分越高，障碍越大）
# 题目间有正相关（一个障碍高，其他障碍也高）
latent_obstacle = np.random.normal(0, 1, n)

obstacle_q1 = 3 + latent_obstacle * 0.8 + np.random.normal(0, 0.6, n)
obstacle_q2 = 3 + latent_obstacle * 0.8 + np.random.normal(0, 0.6, n)
obstacle_q3 = 3 + latent_obstacle * 0.8 + np.random.normal(0, 0.6, n)

# 量表2：数字能力（得分越高，能力越强）
# 题目间有正相关（一个能力强，其他能力也强）
latent_ability = np.random.normal(0, 1, n)

ability_q1 = 3 + latent_ability * 0.9 + np.random.normal(0, 0.5, n)
ability_q2 = 3 + latent_ability * 0.9 + np.random.normal(0, 0.5, n)
ability_q3 = 3 + latent_ability * 0.9 + np.random.normal(0, 0.5, n)
ability_q4 = 3 + latent_ability * 0.9 + np.random.normal(0, 0.5, n)

# 合并为DataFrame，限制1-5分
data = pd.DataFrame({
    # 数字障碍量表（3题）
    '障碍1_看不懂': np.clip(obstacle_q1, 1, 5).round(),
    '障碍2_不会用': np.clip(obstacle_q2, 1, 5).round(),
    '障碍3_没人教': np.clip(obstacle_q3, 1, 5).round(),
    # 数字能力量表（4题）
    '能力1_独立操作': np.clip(ability_q1, 1, 5).round(),
    '能力2_信息获取': np.clip(ability_q2, 1, 5).round(),
    '能力3_社区参与': np.clip(ability_q3, 1, 5).round(),
    '能力4_社交网络': np.clip(ability_q4, 1, 5).round(),
})

# ============================================================
# Cronbach's α 函数
# ============================================================

def cronbach_alpha(df):
    """计算Cronbach's α信度系数"""
    df = df.astype(float)
    item_variances = df.var(axis=0, ddof=1)
    total_variance = df.sum(axis=1).var(ddof=1)
    k = df.shape[1]
    return (k / (k - 1)) * (1 - item_variances.sum() / total_variance)

# ============================================================
# 分别计算两个量表的信度
# ============================================================

obstacle_items = data[['障碍1_看不懂', '障碍2_不会用', '障碍3_没人教']]
ability_items = data[['能力1_独立操作', '能力2_信息获取', '能力3_社区参与', '能力4_社交网络']]

alpha_obstacle = cronbach_alpha(obstacle_items)
alpha_ability = cronbach_alpha(ability_items)

print("=" * 60)
print("李克特量表信度检验（Cronbach's α）")
print("=" * 60)
print(f"\n量表1：数字障碍量表（3题）")
print(f"  Cronbach's α = {alpha_obstacle:.3f}")
print(f"  信度等级：{'良好' if alpha_obstacle >= 0.7 else '可接受' if alpha_obstacle >= 0.6 else '不足'}")

print(f"\n量表2：数字能力量表（4题）")
print(f"  Cronbach's α = {alpha_ability:.3f}")
print(f"  信度等级：{'良好' if alpha_ability >= 0.7 else '可接受' if alpha_ability >= 0.6 else '不足'}")

print("\n" + "=" * 60)
print("判断标准：")
print("  α ≥ 0.9 → 非常好")
print("  0.7 ≤ α < 0.9 → 良好")
print("  0.6 ≤ α < 0.7 → 可接受")
print("  α < 0.6 → 不足，需修订")

# ============================================================
# 绘制箱线图
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左边：数字障碍量表
obstacle_items.boxplot(ax=axes[0])
axes[0].set_title(f'数字障碍量表（3题）\nCronbach\'s α = {alpha_obstacle:.3f}')
axes[0].set_ylabel('得分（1-5分）')
axes[0].set_xlabel('题目')
axes[0].set_xticklabels(['看不懂', '不会用', '没人教'])

# 右边：数字能力量表
ability_items.boxplot(ax=axes[1])
axes[1].set_title(f'数字能力量表（4题）\nCronbach\'s α = {alpha_ability:.3f}')
axes[1].set_ylabel('得分（1-5分）')
axes[1].set_xlabel('题目')
axes[1].set_xticklabels(['独立操作', '信息获取', '社区参与', '社交网络'])

plt.tight_layout()
plt.savefig('likert_reliability.png', dpi=150)
plt.show()

print("\n✅ 图表已保存: likert_reliability.png")