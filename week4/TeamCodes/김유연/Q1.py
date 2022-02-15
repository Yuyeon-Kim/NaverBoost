# 220214
# Q1

import pandas as pd

idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

# 위 데이터로 Series 구현
series = pd.Series(data, index = idx)

# 10 이상 20 이하 series 정의
series = series[series >= 10][series <= 20]

print(series)