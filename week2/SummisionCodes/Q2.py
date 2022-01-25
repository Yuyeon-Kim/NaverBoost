# 220124

# Q2. 다양한 탈 것을 사용하는 게임을 만드는 중입니다. 빠른 구현을 위해서 이미 구현한 Car 클래스를 이용해서 Bike라는 클래스를 새로 제작하려고 합니다. Car 클래스를 상속받아서 새로운 Bike 클래스를 아래와 같이 출력되도록 구성해보세요.
# - Bike class는 size 인자를 추가로 가집니다.

class Car():
    def __init__(self, fuel, wheels): # Car 생성자
        self.fuel = fuel # pyblic 멤버변수 fuel에 초기값 저장
        self.wheels = wheels # public 멤버변수 wheels에 초기값 저장
    
class Bike(Car): # Car 클래스 상속
    def __init__(self, fuel, wheels, size): # Bike 생성자
        super().__init__(fuel, wheels) # 부모 클래스의 생성자 호출
        self.size = size # public 멤버변수 size

bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)

# 출력
# gas 2 small