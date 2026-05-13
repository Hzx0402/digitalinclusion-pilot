# 李克特量表信度检验
# 生成合理模拟数据 + 中文图表

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(42)
n = 200

# ============================================================
# 生成合理的模拟数据（题目间有正相关）
# ============================================================

# 个人障碍维度：3个问题，设定相关系数0.6
np.random.seed(42)
latent_obstacle = np.random.normal(0, 1, n)

obstacle_q1 = 3 + latent_obstacle * 0.8 + np.random.normal(0, 0.6, n)
obstacle_q2 = 3 + latent_obstacle * 0.8 + np.random.normal(0, 0.6, n)
obstacle_q3 = 3 + latent_obstacle * 0.8 + np.random.normal(0, 0.6, n)

# 实际核心能力维度：4个问题，设定相关系数0.7
latent_ability = np.random.normal(0, 1, n)

ability_q1 = 3 + latent_ability * 0.9 + np.random.normal(0, 0.5, n)
ability_q2 = 3 + latent_ability * 0.9 + np.random.normal(0, 0.5, n)
ability_q3 = 3 + latent_ability * 0.9 + np.random.normal(0, 0.5, n)
ability_q4 = 3 + latent_ability * 0.9 + np.random.normal(0, 0.5, n)

# 合并为DataFrame，限制1-5分
data = pd.DataFrame({
    '障碍_可获得性': np.clip(obstacle_q1, 1, 5).round(),
    '障碍_技能': np.clip(obstacle_q2, 1, 5).round(),
    '障碍_有效使用': np.clip(obstacle_q3, 1, 5).round(),
    '能力_社区参与': np.clip(ability_q1, 1, 5).round(),
    '能力_信息获取': np.clip(ability_q2, 1, 5).round(),
    '能力_社交网络': np.clip(ability_q3, 1, 5).round(),
    '能力_经济机会': np.clip(ability_q4, 1, 5).round(),
})

# ============================================================
# 计算 Cronbach's α
# ============================================================

def cronbach_alpha(df):
    df = df.astype(float)
    item_variances = df.var(axis=0, ddof=1)
    total_variance = df.sum(axis=1).var(ddof=1)
    k = df.shape[1]
    return (k / (k - 1)) * (1 - item_variances.sum() / total_variance)

obstacle_items = data[['障碍_可获得性', '障碍_技能', '障碍_有效使用']]
ability_items = data[['能力_社区参与', '能力_信息获取', '能力_社交网络', '能力_经济机会']]

alpha_obstacle = cronbach_alpha(obstacle_items)
alpha_ability = cronbach_alpha(ability_items)

print("=" * 50)
print("李克特量表信度检验（Cronbach's α）")
print("=" * 50)
print(f"个人障碍（3题）: α = {alpha_obstacle:.3f}")
print(f"实际核心能力（4题）: α = {alpha_ability:.3f}")

# 信度等级
def grade(alpha):
    if alpha >= 0.9: return "非常好"
    if alpha >= 0.7: return "良好"
    if alpha >= 0.6: return "可接受"
    return "不足"

print(f"\n个人障碍信度等级: {grade(alpha_obstacle)}")
print(f"实际核心能力信度等级: {grade(alpha_ability)}")

# ============================================================
# 绘制箱线图（中文标题）
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左边：个人障碍
obstacle_items.boxplot(ax=axes[0])
axes[0].set_title(f'个人障碍各题得分分布\n(Cronbach\'s α = {alpha_obstacle:.3f})', fontsize=12)
axes[0].set_ylabel('得分（1-5分）')
axes[0].set_xlabel('题目')

# 右边：实际核心能力
ability_items.boxplot(ax=axes[1])
axes[1].set_title(f'实际核心能力各题得分分布\n(Cronbach\'s α = {alpha_ability:.3f})', fontsize=12)
axes[1].set_ylabel('得分（1-5分）')
axes[1].set_xlabel('题目')

plt.tight_layout()
plt.savefig('likert_reliability.png', dpi=150)
plt.show()

print("\n✅ 图表已保存: likert_reliarity.png")