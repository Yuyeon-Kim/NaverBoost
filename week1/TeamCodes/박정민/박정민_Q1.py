# 제출 코드
num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
  odd_num = []
  for number in num_list:
    if number % 2 == 1:
      odd_num.append(number)
  return odd_num

print(get_odd_num(num_list))