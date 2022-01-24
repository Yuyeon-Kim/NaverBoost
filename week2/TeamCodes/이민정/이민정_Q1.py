#중간고사 기말고사 점수를 따로 받아 저장하는 클래스
#생성자의 인스턴스는 private으로 선언
#decorator를 이용해 데이터 저장
#함수를 이용해 평균값 출력
#hint: 자료형의 선언과 데코레이터 이용

#test score, mid: 50, final: 75

class Score():
    def __init__(self, mid, final):
        self.mid = float(mid)
        self.final = float(final)

score = Score(50, 75)
print((score.mid + score.final) / 2)