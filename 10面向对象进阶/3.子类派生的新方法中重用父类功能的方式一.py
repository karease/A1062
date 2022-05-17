'''
子类重用父类的功能
在子类派生出的新方法中重用父类功能的方式一
指名道姓地引用某一个类中的函数
'''

class People:
    school = '图灵学院'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

class Student(People):
    def __init__(self,name,age,sex,score=0):
        People.__init__(self,name,age,sex)
        self.score=score
    def play(self):
        print('%s play football' % self.name)

class Teacher(People):
    # def __init__(self,name,age,sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    def course(self):
        print('%s course' % self.name)