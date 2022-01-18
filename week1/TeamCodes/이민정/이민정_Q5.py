# string 안에서의 숫자 제거 후 string만 남은 리스트를 출력

# 구현하고 싶은 코드: string을 처음부터 탐색한 다음
# 숫자가 나오면 끊은 다음 리스트 요소로 만들고 싶어요

inputs = "cat32dog16cow5"

def find_string(inputs):
    for i in inputs:
        if i.isdigit():
            print(i)
    

string_list = find_string(inputs)
print(string_list)

#결과: ['cat', 'dog', 'cow']