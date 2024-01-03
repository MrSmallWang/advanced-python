import pandas as pd

# 创建一个示例DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

"""取出元素"""
for i in range(3):
    element = df.iloc[i, 1]
    print(element, type(element))



print(df)
# 使用itertuples()遍历DataFrame的每一行
for row in df.itertuples():
    # print(f'Index: {row.Index}, Name: {row.Name}, Age: {row.Age}')
    print(type(row))
    # print(row.Name)
