# 所有的加了引号的数据类型都是字符串类型
# print(type('17')) # <class 'str'>
# print(type(17)) # <class 'int'>
#
# #一：数字类型 *****
# # 整型int
# #作用：记录年龄，等级，QQ号，各种号码
# # 定义
# age = 18
# print(age)
# print(type(age))
# # 2.浮点型：float
# #作用：记录身高、体重weight、薪资
# #定义：
# weight = 130.4
# print(weight)
# print(type(weight))
# print(weight)
# print(weight)
# print(weight)
#不可变类型
# age = 18
# print(age)
# print(id(age))
# age = 20
# print(age)
# print(id(age))

# 赋值运算
# 普通赋值 =
# 加法赋值 +=
# 减法赋值 -=
# 乘法赋值 *=
# 除法赋值 /=
# 取余赋值 %=
# 乘方赋值 **=
# 地板除赋值 //=

# 语法 n = n + XXX 相等于 n += XXX
n = 2
# n = n + 3
# 等价
# n += 3
# print(n)
# n -= 1    #等价于 n=n-1
# print(n)

n /= 1 #等价于 n=n/1
print(int(n))