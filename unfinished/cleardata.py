import pandas as pd

for i in range(7):
    data = pd.read_csv('wp'+str(i+1)+'dat', delim_whitespace=True, skiprows=3, header=None, usecols=[0, 1])
    data.columns = ['time', 'p']

    data['time'] = data['time'].astype(float)

    output_file = './clear/' + str(i+1) + 'wcleaned.csv'
    data.to_csv(output_file, index=False)

    print(f"数据已清洗并保存到 {output_file}")
