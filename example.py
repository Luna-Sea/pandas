import pandas as pd
WriteLine = print
import matplotlib.pyplot as plt

data = pd.read_csv("abalone.txt", sep=',')
#返回是整个二维表格 DataFrame对象
WriteLine(data)          #输出所有行

#for e in data:
#    print(e)
#输出列名

sex_column = data['Sex'] #只获取Sex列
WriteLine(sex_column)    #输出所有行

male_data = data[data['Whole'] == 0.514]
WriteLine(male_data) # 获取Whole == 0，0514的所有列
#male_data.to_csv('male_data.csv', index=False)         #保存至某个文件

male_length = male_data['Shell'].tolist() #将Shell列转化为List
print(male_length)#将male_data中Shell列转化为列表
#for e in male_length:
#    WriteLine(e)

#selectrow  = male_data.loc[553]        #获取索引为553的行
#print(selectrow)

#以pandas的DataFrame对象中的Length和Diameter，绘制散点图（scatter） 折线图（line）
#柱形图（bar） 水平柱状图（barh）
male_data.plot(x='Length', y='Diameter', kind='scatter')
plt.show()

#分组
sex_data = data.groupby('Sex')['Diameter'].mean()
#mean max min count  聚合函数
WriteLine(sex_data)
