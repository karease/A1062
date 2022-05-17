'''
1 初始化
以双下划线开头且以双下划线结尾的固定方法，它会在特定的时机被触发执行
'''
class Teacher:
    #相同的特征、属性、变量
    school = 'GXNU'
    #这个不对，不应该定义为类属性
    # name = '仰容生'
    #
    # age = 19
    # sex = '男'

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    #函数 方法 技能
    def course(self,name):
        #self到底是什么？
        #self当做一个位置参数
        print(self)
        print('course')
        print(name)
        print('------------------')
        print('我是仰容生的属性%s'%self.name)
        print('我是仰容生的属性%s'%self.age)
        return '11111'

#产生3个老师对象
#__init__没有就没有独有的对象属性
#t1=Teacher()
#print(t1.__dict__)

#有__init__方法  有了对象独有的属性
yrs = Teacher('仰容生',22,'男')
xialuo = Teacher('夏洛',21,'男')
xishi = Teacher('西施',12,'女')
#对象的独立属性
# print(yrs.__dict__)
# print(xialuo.__dict__)
# print(xishi.__dict__)
#
# #类的属性 对象调用和类调用一样
# print(yrs.school)
# print(id(yrs.school))
#
# print(Teacher.school)
# print(id(Teacher.school))

# print(yrs)
# #对象独立的属性
# print(yrs.__dict__)
#
# #对象独立的属性
# print(xialuo)
# print(xialuo.__dict__)

#__init__方法传入的属性类是没有的
#print(Teacher.__dict__)

#只是初始化时传入了参数  对象还可以改属性值
# print(yrs.name)
# yrs.name = 'aka'
# print(yrs.__dict__)

a1 = yrs.course('yrrrrr')
print(a1)