# 문제: 
# string 문장을 받아 단어를 역순으로 출력하는 함수를 작성하세요.

sentence = "way a is there will a is there where"

def reverse_sentence(sentence):
    sentence = sentence.split() # 띄어쓰기 단위로 split하여 리스트로 저장
    sentence.reverse() # 리스트 원소 순서 역순으로 바꾸기
    sentence = " ".join(sentence) # 띄어쓰기를 각 원소의 사이에 놓고, string으로 합치기
    return sentence # 결과 string return

print(reverse_sentence(sentence))

# 출력
# where there is a will there is a way