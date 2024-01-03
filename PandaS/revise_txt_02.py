import pandas as pd
import numpy as np

data = "samples_shu.txt"

df = pd.read_csv(data, sep=" ", error_bad_lines=False, header=None, names=range(30), )
df = df.fillna(value=" ")
value = df.iloc[1, 0]
print(f'"{value}"')
print(f'"{df.iloc[1, 1]}"')

with open("output_911_shu_04.txt", mode="w", encoding="utf-8", ) as f:
# with open("output_911_ping.txt", mode="w", encoding="utf-8", ) as f:
    for i in range(df.shape[0]):
        if df.iloc[i, 3] != "0":
            # print(type(df.iloc[i, 3]), df.iloc[i, 3], df.iloc[i, 2], df.iloc[i, 1], df.iloc[i, 0])
            output_string = " ".join(map(str, df.iloc[i].values))
            f.write(output_string)
            f.write("\n")
            continue # 如果不写continue那么else的代码也会被执行，keep in attention!
        if df.iloc[i, 3] == "0" and df.iloc[i-1, 3] == "0":
            # output_string = " ".join(map(str, df.iloc[i-1].values))
            # print(type(df.iloc[i-1, 3]), df.iloc[i-1, 3], df.iloc[i-1, 2], df.iloc[i-1, 1], df.iloc[i-1, 0])
            # f.write(output_string)
            # f.write("\n")
            df.iloc[i, 0], df.iloc[i, 1] = str(f'"{df.iloc[i, 0]}"'), str(f'"{df.iloc[i, 1]}"')
            mu = float(df.iloc[i-1, 7])
            df.iloc[i, 7] = str(round(np.random.normal(mu, 0.05), 5))
            df.iloc[i, 10], df.iloc[i, 13], df.iloc[i, 16]= df.iloc[i, 7], df.iloc[i, 7], df.iloc[i, 7]
            output_string = " ".join(map(str, df.iloc[i].values))
            # print(output_string)
            f.write(output_string)
            f.write("\n")
        else:
            df.iloc[i, 0], df.iloc[i, 1] = str(f'"{df.iloc[i, 0]}"'), str(f'"{df.iloc[i, 1]}"')
            output_string = " ".join(map(str, df.iloc[i].values))
            f.write(output_string)
            f.write("\n")


