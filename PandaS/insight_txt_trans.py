import pandas as pd

# data = "test_01.txt"
data = "sanples.txt"

df = pd.read_csv(data, sep=" ", error_bad_lines=False, header=None, names=range(30))
df = df.fillna(value=" ")

print(df.iloc[1, 3])

output_string = " ".join(map(str, df.iloc[1].values))
# def s_c(row):
#     return pd.Series(row[0].split(" "))
#
#
# new_df = df.apply(s_c, axis=1)

with open("output_08.txt", "w", encoding="utf-8") as f:
    f.write(output_string)


print(df.iloc[1])
print(output_string)
# print(new_df.iloc[1])
print(type(df.iloc[1, 7]))
print(df.iloc[1, 7])