'''

'''

#1 先定义类
class Teacher:
    #相同的特征、属性、变量
    name = '仰容生'
    age = 19
    sex = '男'

    #函数 方法 技能
    def course(self):
        #self到底是什么？
        #self当做一个位置参数
        print(self)
        print('course')
        return 222
#2、后调用类来产生对象：
#调用类的过程称之为类的实例的初始化，调用类的返回值称之为类的一个对象/实例
#类是抽象  对象/实例是具象


#产生3个老师对象
t1=Teacher()
t2=Teacher()
t3=Teacher()

# print(t1)
# print(id(t2))
# print(id(t3))
# print(id(t1))

#对象独有的属性
# print(t1.__dict__)
#
# print(t1.name)
# print(t2.name)
# print(t3.name)

#对象的方法 （没有独有的，从类里面去要）
# print(t1.course())
# print(t2.course())
# print(t3.course())

# print(Teacher.__dict__)
# print('==========')
# print(t1.__dict__)
# print(t2.__dict__)
# print(t3.__dict__)

#类有return
#aaa=Teacher.course(111)
#print(aaa)

#对象的方法

#对象的方法执行，没有传入参数  self到底是什么
#对比类方法执行 需要传入参数
# print(t1)
# a1 = t1.course()
# print(a1)

#对象的属性修改
#(类里面的属性)
# print(t1.name)
# print(t1.__dict__)
# #添加了对象独有的属性
t1.name = '夏洛'
# print(t1.name)
# print(t1.__dict__)
#
#
# #删除对象的属性
# #删除的是  t1.name = '夏洛'
# del t1.name
print(t1.name)

#对象完全独立 一个对象的操作不会对另外一个对象产生影响
print(t2.name)
