# string 연산을 이용해서 문자열을 자르는 연산을 사용해보세요.

inputs = "cat32dog16cow"

def find_string(inputs: str):
    # TODO
    res = [] # 결과 저장할 리스트
    temp_str="" # 끊기지 않은 스트링들 저장할 변수
    for s1, s2 in zip(inputs, inputs[1:]+"0"):
        if not s1.isnumeric():
            temp_str+=s1
            if s2.isnumeric():
                res.append(temp_str)
                temp_str = ""
    return res

string_list = find_string(inputs)
print(string_list)

# 출력 
# ['cat', 'dog', 'cow']