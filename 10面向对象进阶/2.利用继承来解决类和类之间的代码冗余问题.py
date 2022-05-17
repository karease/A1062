'''
 2.利用继承来解决类和类之间的代码冗余问题

 总结对象的相似之处得到了类
 总结类的相似之处得到父类
'''

class People:
    school = '图灵学院'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

class Student(People):
    # def __init__(self,name,age,sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    def play(self):
        print('%s play football' % self.name)

class Teacher(People):
    # def __init__(self,name,age,sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    def course(self):
        print('%s course' % self.name)

#实例化时子类没有__init__方法会调用父类的
stu1 = Student('周阳',30,'male')
print(stu1.__dict__)
tea1 = Student('大海',20,'male')
print(tea1.__dict__)
