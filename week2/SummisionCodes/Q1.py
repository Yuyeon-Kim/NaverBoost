# 220124

# Q1. 중간고사 기말고사 점수를 따로 받아 저장하는 클래스를 구현해보세요. 단, 생성자의 인스턴스는 private으로 선언되어야하며, 데코레이터를 이용해 데이터를 저장하고, 함수를 이용해 평균값을 출력해보세요.
# - 자료형의 선언과 데코레이터를 이용해보세요.
# test score, mid : 50, final : 75

class Score():
    def __init__(self, mid : int, final : int):
        self.__mid = mid # private 멤버변수 mid에 초기값 저장
        self.__final = final # private 멤버변수 final에 초기값 저장

    @property # property 데코레이터를 사용해 클래스 외부에서 mid가 attribute로 작동하도록 한다.
    def mid(self):
        return self.__mid # private 변수 __mid return
    
    @property # property 데코레이터를 사용해 클래스 외부에서 mid가 attribute로 작동하도록 한다.
    def final(self):
        return self.__final # private 변수 __mid return

# 출력 함수
score = Score(50, 75)
print((score.mid + score.final) / 2)

# 출력
# 62.5