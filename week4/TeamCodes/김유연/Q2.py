# 220214
# Q2

import pandas as pd

df1 = pd.DataFrame([
["cherry", "Fruit", 100],
["mango", "Fruit", 110],
["potato", "Vegitable", 60],
["onion", "Vegitable", 80]],
columns = ["Name", "Type", "Price"])

df2 = pd.DataFrame([
["pepper", "Vegitable", 50],
["carrot", "Vegitable", 70],
["banana", "Fruit", 90],
["kiwi", "Fruit", 120]],
columns = ["Name", "Type", "Price"])

# df1, df2 결합
df3 = pd.concat([df1, df2], axis = 0)

# fruit과 vegitable type에 따라 정렬, 내림차순 정리
df_fruit = df3.loc[df3["Type"] == "Fruit"].sort_values(by = "Price", ascending = False)

df_veg = df3.loc[df3["Type"] == "Vegitable"].sort_values(by = "Price", ascending = False)

# fruit와 vegitable 상위 2개의 가격 합 출력
print("Sum of Top 2 Fruit Price : ", sum(df_fruit[:2]["Price"]))
print("Sum of Top 2 Vegitable Price : ", sum(df_veg[:2]["Price"]))