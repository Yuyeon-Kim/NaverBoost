# 문제: 
# string 연산을 이용해서 문자열을 자르는 연산을 사용해보세요.

inputs = "cat32dog16cow"

def find_string(inputs: str):
    res = [] # 결과 저장할 빈 리스트
    temp_str="" # 끊기지 않은 스트링들 저장할 변수
    for s1, s2 in zip(inputs, inputs[1:]+"0"): # s1과 그 다음 글자 s2, 길이를 맞추기 위해 "0" 추가
        if not s1.isnumeric(): # s1이 글자이면
            temp_str+=s1 # 끊기지 않은 스트링에 해당 글자 저장
            if s2.isnumeric(): # s2가 숫자이면
                res.append(temp_str) # 끊기지 않은 스트링을 결과 리스트에 저장
                temp_str = "" # 끊기지 않은 스트링 변수 초기화
    return res

string_list = find_string(inputs)
print(string_list)

# 출력 
# ['cat', 'dog', 'cow']