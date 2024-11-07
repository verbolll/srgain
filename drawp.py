import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False
# 定义文件名称
filenames = [f".\\clear\\{i}wcleaned.csv" for i in range(1, 8)]
filenamesy = [f".\\clear\\{i}cleaned.csv" for i in range(1, 8)]
fig, ax = plt.subplots() 
# 创建一个图形
# plt.figure(figsize=(10, 6))

ii = 1
# 读取每个文件并绘制折线图
for filename in filenames:
    # 读取CSV文件
    data = pd.read_csv(filename)
    
    # 绘制曲线，time为横坐标，p为纵坐标
    ax.plot(data['time'], data['p'], label=f'第{ii}号，无侵蚀燃烧')
    ii = ii + 1
ii = 1
for filename in filenamesy:
    # 读取CSV文件
    data = pd.read_csv(filename)
    
    # 绘制曲线，time为横坐标，p为纵坐标
    ax.plot(data['time'], data['p'], '--', label=f'第{ii}号，有侵蚀燃烧')
    ii = ii + 1

# 添加图例和标签
ax.set_xlim(-0.2964, 0.4543)
ax.set_ylim(8.037, 9.125)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Time", fontsize=14)
plt.ylabel("p", fontsize=14)
ax.legend(fontsize=10,)
ax.grid()

# 显示图形
# plt.show()
plt.savefig('双图局览左.pdf')
