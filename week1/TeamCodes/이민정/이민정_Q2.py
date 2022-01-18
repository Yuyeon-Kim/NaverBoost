#미션2: 단어 단위로 거꾸로 입력된 문자열을 원래대로 출력

sentence = "way a is there will a is there where"

def reverse_sentence(sentence):
    #공백을 기준으로 잘라서 new 리스트 만들기. 거꾸로 한 칸씩 정렬
    #그 리스트를 다른 변수에 집어넣기
    sorted_sentence = (sentence.split(" ")[::-1])
    for i in sorted_sentence:
        print(i)
    #print(sorted_sentence)

print(reverse_sentence(sentence))