'''
类
    老师
        属性
            name='yrs'
            age=22
            sex='男'
        技能\方法\函数
            上课
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
    #print('类定义是运行的')

#类是一系列对象相同的属性（变量）与技能（函数）的结合体
#即类中最常见的就是变量与函数的定义
#类体代码会在类定义阶段立即执行，会产生一个类的名称空间


# name = 'aaa'
# print(name)
# #print(Teacher.__dict__)
# #调用类的属性
# print(Teacher.name)
# print(Teacher.age)
# print(Teacher.sex)

#类的方法其实就是函数
#print(Teacher.course)

#函数加括号调用
#self 把它当作一个位置形参 但为何定义为self？

#Teacher.course(111)

#不存在的属性或方法会报错
#print(Teacher.xxx)

#修改属性的值
# print(Teacher.name)
# Teacher.name = '夏洛'
# print(Teacher.name)

#添加类的属性
Teacher.play = '篮球'
print(Teacher.play)
print(Teacher.__dict__)

#删除类的属性
del Teacher.play
#print(Teacher.play)
print(Teacher.__dict__)

'''
总结
1、类的本质是一个用来存放变量与函数的容器
2、类的用途之一就是当做容器来从其内部取出名字（变量和函数名）来使用
3、类的用途之二是调用类来产生对象
'''