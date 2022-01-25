# 220113
# 문제: 
# string 문장을 받아 단어를 역순으로 출력하는 함수를 작성하세요.

sentence = "way a is there will a is there where"

def reverse_sentence(sentence):
    return " ".join(reversed(sentence.split()))

print(reverse_sentence(sentence))

# 출력
# where there is a will there is a way