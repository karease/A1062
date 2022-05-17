# class Teacher:
#     #相同的特征、属性、变量
#     school = 'tuling'
#     xxx = '我是类的属性  也可能是对象的属性'
#     yyy = 111
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     #函数 方法 技能
#     def course(self,name):
#         print(self)
#         # print('course')
#         # print(name)
#         # print('------------------')
#         # print('我是仰容生的属性%s'%self.name)
#         # print('我是仰容生的属性%s'%self.age)
#         # return '11111'
#
# #实例初始化时必须传入参数  生成了对象的属性
# dahai = Teacher('大海',18,'男')
# xialuo = Teacher('夏洛',16,'男')
# xishi = Teacher('西施',15,'女')
#
# #对象属性的查找
# #添加一个对象属性
#
# #类中定义的属性和方法是所有对象共享的  类可以用 对象也可以用
# #类的属性给对象调用（原装）
# # print(id(dahai.yyy),dahai.yyy)
# # print(id(xialuo.yyy),xialuo.yyy)
# # print(id(xishi.yyy),xishi.yyy)
#
# #类的属性变化
# #类改类的属性
#
# # Teacher.yyy = 333
# # #对象改类的属性（改不了） （实际上是自己添加了一个独有的属性）
# # dahai.yyy = 222
# #
# # #类的属性给对象调用
# # #对象已经有了yyy属性的会优先考虑自己的
# # print(id(dahai.yyy),dahai.yyy)
# # print(id(xialuo.yyy),xialuo.yyy)
# # print(id(xishi.yyy),xishi.yyy)
#
# print(id(dahai.course))
# dahai.course
#
# print(id(xialuo.course))
# xialuo.course
#
# print(id(xishi.course))
# xishi.course