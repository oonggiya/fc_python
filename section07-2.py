# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브 클래스(자식) -> 모든 속성, 메소드 사용 가능

class Car:
  """Parent Class"""
  def __init__(self, tp, color):
    self.type = tp
    self.color = color

  def show(self):
    return 'Car class "show method!" '


class BmwCar(Car):
  """sub class"""
  def __init__(self, car_name, tp, color):
    super().__init__(tp,color)
    self.car_name = car_name

  def show_model(self):
    return "your car Name : %s" % self.car_name

class BenzCar(Car):
  """sub class"""
  def __init__(self, car_name, tp, color):
    super().__init__(tp,color)
    self.car_name = car_name

  def show_model(self):
    return "your car Name : %s" % self.car_name

  def show(self):
    print(super().show())
    return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

  
# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding

model2 = BenzCar('Glk220', 'Suv', 'White')
print(model2.show())

# Parent Method Call

model3 = BenzCar('S class', 'sedan', 'silver')
print(model3.show())

# Inheritance Info(상속 정보)
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속

class X():
  pass

class Y():
  pass

class Z():
  pass

class A(X, Y):
  pass

class B(Y, Z):
  pass

class M(B, A, Z):
  pass

print(M.mro())
