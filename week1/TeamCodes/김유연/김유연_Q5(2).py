# 220117
# 문제: 
# string 연산을 이용해서 문자열을 자르는 연산을 사용해보세요.

inputs = "cat32dog16cow"

def find_string(inputs: str):
    # TODO
    # "cat  dog  cow"
    return "".join([i if not i.isdigit() else " " for i in inputs ]).split()

string_list = find_string(inputs)
print(string_list)

# 출력 
# ['cat', 'dog', 'cow']