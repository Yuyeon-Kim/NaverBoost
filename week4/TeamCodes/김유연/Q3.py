# 220215
# Q3

import pandas as pd

idx = ["Sue", "Ryan", "Jay", "Jane", "Anna"]
col = ["round_%d"%i for i in range(1, 6)]
data = [[55, 65, 60, 66, 57],
[64, 77, 71, 79, 67],
[88, 81, 79, 89, 77],
[45, 35, 30, 46, 47],
[91, 96, 90, 97, 99]]

# 위 데이터로 dataframe 구성
df = pd.DataFrame(data=data, index=idx, columns=col)

# df에 새로운 column인 round_6의 데이터 [11, 15, 13, 17, 19] 추가
col_round_6 = [11, 15, 13, 17, 19]
df["round_6"] = col_round_6
print(df)

# 각 데이터의 mean, max, min값 출력
print(df.describe().loc[["mean", "max", "min"]])
