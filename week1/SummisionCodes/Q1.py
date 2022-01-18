# 문제 1: 
# num_list 가 홀수인 데이터만 출력하도록 하는 함수를 작성해보세요.

num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
  odd_num = [] # 빈 리스트 odd_num 생성
  for number in num_list: # num_list 내의 값 하나씩 반복
    if number % 2 == 1: # 2로 나눈 나머지가 1이면, 즉, 홀수이면
      odd_num.append(number) # odd_num에 해당 숫자를 append
  return odd_num # odd_num return

print(get_odd_num(num_list))

# 출력
# [1, 5, 7, 15, 29]