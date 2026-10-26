import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Rectangle

csv_file = 'C:/Users/49447/Desktop/hist_marked_root.csv'
low_thresh = 52
high_thresh = 96
df = pd.read_csv(csv_file)
x = df["value"]
y = df["count"]

plt.figure(figsize=(10,7),dpi=300)
plt.bar(x,y,color="#603896",width=1)

# 根系区间红色半透明方框
y_max = 12000
# =========空心方框：边框红色，内部完全透明(facecolor='none')=========
rect = Rectangle((low_thresh, 0),
                 width=high_thresh - low_thresh,
                 height=y_max,
                 linewidth=2,
                 edgecolor='red',
                 facecolor='none')
plt.gca().add_patch(rect)

# ----------箭头标注阈值区间----------
mid_x = (low_thresh + high_thresh)/2
plt.annotate(
    "Threshold region",
    xy=(mid_x-22, 8000),
    xytext=(mid_x-65, 10000),
    fontsize=13,
    arrowprops=dict(arrowstyle="->", color="black", lw=1.5)
)
# =====三处箭头标注=====
# 孔隙
plt.annotate("Air filled pore space",
             xy=(25,1000),
             xytext=(10,2000),
             fontsize=14,
             arrowprops=dict(arrowstyle="->",color='black'))
# 根系（方框中间）
mid_root = (low_thresh+high_thresh)/2
plt.annotate("Root",
             xy=(mid_root, 500),
             xytext=(mid_root+10, 1000),
             fontsize=14,
             arrowprops=dict(arrowstyle="->",color='black'))

plt.gca().add_patch(rect)
# 土壤颗粒（主峰顶点）
plt.annotate("Soil matrix",
             xy=(130, 9600),
             xytext=(135, 11000),
             fontsize=14,
             arrowprops=dict(arrowstyle="->",color='black'))


plt.xlabel("Intensity of grayscale", fontsize=12)
plt.xlim(0, 200)
plt.ylim(0, y_max)
plt.title("Gray‑level histogram of roots", fontsize=18)



plt.savefig("C:/Users/49447/Desktop/image/hist_marked_root.svg",format="svg",bbox_inches="tight")
plt.show()
