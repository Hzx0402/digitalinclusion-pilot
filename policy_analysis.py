# 计算文本分析：政策文件关键词统计
# 研究主题：数字包容、社会公平、广州智慧城市更新

import os

# 获取当前文件所在的文件夹路径
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'policy.txt')

# 读取政策文件
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"成功读取文件：{file_path}\n")
except FileNotFoundError:
    print(f"提示：找不到 policy.txt 文件")
    print(f"查找路径：{file_path}")
    print("请确保 policy.txt 和 policy_analysis.py 在同一个文件夹中")
    exit()

# 定义与研究相关的关键词
keywords = {
    '弱势群体': 0,
    '智慧社区': 0,
    '城市更新': 0,
    '数字包容': 0,
    '数字鸿沟': 0,
    '参与': 0,
    '公平': 0,
    '老年人': 0,
    '安置': 0,
    '一老一小': 0,
    '获得感': 0,
    '幸福感': 0,
    '安全感': 0,
}

# 统计每个词出现的次数
for word in keywords:
    keywords[word] = text.count(word)

# 输出结果
print("=" * 40)
print("广州智慧社区政策文本分析")
print("=" * 40)
print("\n【关键词频率统计】\n")
for word, count in keywords.items():
    if count > 0:
        print(f"  {word}: {count} 次")

# 统计有内容的词总数
total = sum(1 for c in keywords.values() if c > 0)
print(f"\n共找到 {total} 个关键词出现在文本中")
print("=" * 40)