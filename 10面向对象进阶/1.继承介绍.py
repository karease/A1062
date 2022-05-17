'''

1 什么是继承
    继承是一种新建类的方法 新建的类称之为子类/派生类  被继承的类叫做父类、基类、
    '''

class Parent1:
    xxx = 333
    def run(self):
        print('我是父类方法')

class Sub1(Parent1):
   # xxx = 222
    #def run(self):
        #print('我是子类方法')
    pass

obj = Sub1()
#obj.xxx = 111

#对象<<类<<父类

print(obj.xxx)
obj.run()