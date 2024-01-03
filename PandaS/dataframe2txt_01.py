import pandas as pd

data = {'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C'],
        'Column3': [4.5, 5.6, 6.7],
        'Column4': ['X', 'Y', 'Z'],
        'Column5': [7, 8, 9]}

df = pd.DataFrame(data)

row_data = df.iloc[0]
print(df)
print(row_data)

with open("output_05.txt", mode="w") as f:
    for item in row_data: # 似乎是这里遍历了每个元素而不是df的一整行所以能得到想要的输出形式
        f.write(str(item) + " ")
    f.write("\n")