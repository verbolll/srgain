import pandas as pd

for i in range(7):
    # # 读取文件内容，跳过前三行的标题部分
    data = pd.read_csv('wp'+str(i+1)+'dat', delim_whitespace=True, skiprows=3, header=None, usecols=[0, 1])
    data.columns = ['time', 'p']  # 设置列名

    # 将包含E的科学计数法转换为浮点数
    data['time'] = data['time'].astype(float)

    # 保存为CSV文件
    output_file = './clear/' + str(i+1) + 'wcleaned.csv'
    data.to_csv(output_file, index=False)

    print(f"数据已清洗并保存到 {output_file}")
