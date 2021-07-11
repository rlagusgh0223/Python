"""
from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse
sleep(1)
mylib.add_txt('나는','파이썬이다')
reverse(1,2,3)
#####################
import mypackage as mp
import mypackage.mylib as ml
ret1 = mp.mylib.add_txt('대한민국','1등')
ret2 = ml.reverse(1,2,3)
#####################
f1 = open('test.txt','r')
f2 = open('C:/Users/Owner/Desktop/khh/python\mypackage\picture.jpg','rb')
print("동작")
f1.close()
f2.close()

###################
class Myclass:
    var='안녕하세요'
    def sayHello(self):
        print(self.var)
obj=Myclass()
print(obj.var)
obj.sayHello()
"""
##################
class MyClass:
    var='안녕하세요!'
    def sayHello(self):
        param1='안녕'
        self.param2='하이'
        print(param1)
        print(self.var)

obj=MyClass()
print(obj.var)
obj.sayHello()


