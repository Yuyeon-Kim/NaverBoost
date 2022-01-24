# 이미 구현한 Car 클래스를 이용해서 Bike라는 클래스를 새로 제작하려고 합니다
# Car 클래스를 상속받아서 새로운 Bike 클래스를 아래와 같이 출력되도록 구성해보세요.
#hint: bike class는 size 인자를 추가로 가진다.

class Car():
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels

class Bike(Car):
    def __init__(self, fuel, wheels, size):
        super().__init__(fuel, wheels)
        self.size = size

bike = Bike("gas", 2, "small")

print(bike.fuel, bike.wheels, bike.size)

# 출력값
# gas 2 small