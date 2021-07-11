class MyClass:
    def sayHello(self):
        print('안녕하세요')
    def sayBye(self,name):
        print('%s! 다음에 보자!'%name)
obj = MyClass()
obj.sayHello()
obj.sayBye('철수')
###########################
class MyClass:
    #def __init__(self):
      #  self.var='안녕하세요!'
       # print('MyClass 인스턴스 객체가 생성되었습니다.')
    def __init__(self,txt):
        self.var=txt
        print('생성인자로 전달받은 값은 <'+self.var+'>입니다')
#obj=MyClass()
obj=MyClass('철수')
print(obj.var)
########################

class MyClass:
    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')
obj=MyClass()
del obj
########################
class Add:
    def add(self, n1, n2):
        return n1+n2
class Calculator(Add):
    def sub(self,n1,n2):
        return n1-n2
obj=Calculator()
print(obj.add(1,2))
print(obj.sub(1,2))
###########################
class Add:
    def add(self, n1, n2):
        return n1+n2
class Multiply:
    def multiply(self, n1,n2):
        return n1*n2
class Calculator(Add,Multiply):
    def sub(self,n1,n2):
        return n1-n2
obj=Calculator()
print(obj.add(1,2))
print(obj.multiply(3,2))
##########################
try:
    print('안녕하세요')
    print(poaram)
except:
    print('예외가 발생했습니다.')

