import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False

filenames = [f".\\clear\\{i}wcleaned.csv" for i in range(1, 8)]
filenamesy = [f".\\clear\\{i}cleaned.csv" for i in range(1, 8)]
fig, ax = plt.subplots() 


ii = 1
for filename in filenames:
    data = pd.read_csv(filename)
    ax.plot(data['time'], data['p'], label=f'第{ii}号，无侵蚀燃烧')
    ii = ii + 1
ii = 1
for filename in filenamesy:
    data = pd.read_csv(filename)
    ax.plot(data['time'], data['p'], '--', label=f'第{ii}号，有侵蚀燃烧')
    ii = ii + 1

# ax.set_xlim(5.786, 6.728)
# ax.set_ylim(7.903, 9.932)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Time", fontsize=14)
plt.ylabel("p", fontsize=14)
ax.legend(fontsize=10, ncol = 1)
ax.grid()

plt.show()
