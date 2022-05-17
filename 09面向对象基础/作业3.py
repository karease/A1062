class Student:
    school = '清华大学'
    address = '北京市海淀区双清路30号'

    def __init__(self,name,age,sex,number):
        self.name   = name
        self.age    = age
        self.sex    = sex
        self.number = number

    def introduce(self):
        print('大家好，我的名字是%s，今年%d岁了，我来自%s，我的学号是%d，请大家多多指教！'%(self.name,self.age,self.school,self.number))

xiaoming = Student('小明',18,'男',171)
xiaoming.introduce()