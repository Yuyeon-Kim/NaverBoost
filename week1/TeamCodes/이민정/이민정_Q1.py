#미션1: num_list 가 홀수인 데이터만 출력하도록 하는 함수를 작성해보세요.

num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    t = [] #빈 리스트 t만들기
    for i in range(0, len(num_list)-1): #반복문: 0부터 리스트의 전체 길이-1 까지만큼 반복
        if num_list[i] % 2 != 0: #만약 리스트에 있는 값이 홀수라면 (2로 나누었을 때 나머지가 0이 아님)
            t.append(num_list[i]) #그 값을 t 리스트에 추가
    return t #t를 반환함

print(get_odd_num(num_list))