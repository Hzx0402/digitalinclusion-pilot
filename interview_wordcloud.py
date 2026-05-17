# 访谈文本分析（使用 THULAC 分词）
import thulac
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re
import os

# ============================================================
# 设置 matplotlib 全局中文字体
# ============================================================
plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang SC', 'Hiragino Sans GB']
plt.rcParams['axes.unicode_minus'] = False

# ============================================================
# 自动检测可用的中文字体（用于词云）
# ============================================================
def find_chinese_font():
    font_paths = [
        '/System/Library/Fonts/STHeiti Light.ttc',
        '/System/Library/Fonts/PingFang.ttc',
        '/System/Library/Fonts/Hiragino Sans GB.ttc',
    ]
    for path in font_paths:
        if os.path.exists(path):
            return path
    return None

# ============================================================
# 访谈文本
# ============================================================
interview_text = """
我不会用智能手机，子女不在身边，没人教我。手机就是接接电话，其他功能都不会用。
看病预约要在手机上操作，我弄不来，每次都要找别人帮忙。
App太复杂了，打开以后不知道点哪里，怕点坏了。
我妈不会用手机交水电费，每次都要等我回家弄。我说教她，她说学不会，怕把手机弄坏了。
微信是别人帮我装的，我就会接视频，别的都不敢点，怕点错了。
社区通知都在手机上，我眼睛看不清，以前还会贴楼下。
子女太忙了，问多了他们也烦，后来我就不问了。
我们几个老人在一起会互相问，这个怎么弄，那个怎么弄。
我也想学，但是眼睛看不清屏幕上的字，字太小了。
那些功能我用不着，能打电话就行了。
不敢绑定银行卡，怕被骗，钱就没了。
村里有人来教过用手机，但是讲得太快，记不住，过后又忘了。
年纪大了，脑子也慢了，用手机也就是回回电话，看看孙子发发照片。
退休后总觉得生活没什么意思，平时儿子忙，孙子也在上学。
社区里的智能机器人也是我的好朋友了，语音对话功能特别简单。
人老了以后，有时候挺想参加参加活动的，但有时候又抹不开面子。
今天这个活动我是很满意的，感觉自己有用了，有成就感！
"""

# ============================================================
# 清洗 + 分词
# ============================================================
text_clean = re.sub(r'[^\u4e00-\u9fa5]', '', interview_text)

thu = thulac.thulac(seg_only=True)
words = thu.cut(text_clean, text=True).split()

stopwords = {'的', '了', '是', '在', '和', '有', '我', '你', '他', '她',
             '也', '就', '都', '不', '会', '能', '这', '那', '人', '们'}
words_filtered = [w for w in words if w not in stopwords and len(w) >= 2]

word_counts = Counter(words_filtered)
print("=" * 50)
print("访谈高频词 Top 15")
print("=" * 50)
for word, count in word_counts.most_common(15):
    print(f"  {word}: {count} 次")

# ============================================================
# 生成词云
# ============================================================
font_path = find_chinese_font()
if font_path:
    print(f"使用字体: {font_path}")
    wc = WordCloud(width=800, height=400, background_color='white',
                   font_path=font_path, colormap='viridis')
else:
    print("未找到中文字体，使用默认字体")
    wc = WordCloud(width=800, height=400, background_color='white', colormap='viridis')

wc.generate_from_frequencies(word_counts)

# ============================================================
# 显示并保存（标题现在会用中文字体）
# ============================================================
plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('访谈词云（THULAC分词 | 基于三篇论文访谈记录）', fontsize=14)
plt.tight_layout()
plt.savefig('interview_wordcloud.png', dpi=150)
plt.show()

print("\n✅ 词云图已保存: interview_wordcloud.png")