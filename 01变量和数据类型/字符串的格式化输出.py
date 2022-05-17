'''
#程序中常会有这样的场景：要求用户输入信息 然后打印成固定的格式
#       比如要求用户输入用户名和年龄 然后打印如下格式
#       My name is xxx,my age is xxx.
这就用到了占位符，如 %s %d
'''

# name = input('请输入名字')
# ##   %s占位符 可接受字符和数字 %d只能接受数字 有局限性
# print('My name is %s.'%name)
#
# # %d
# age = input('请输入年龄')
# # print(age)
# # print(type(age)) #<class 'str'>
#
# age = int(age)
# print(age)
# print(type(age)) #<class 'int'>
#一个值就直接放在%后

#多个值就直接放在%后（要有括号）：
name = input('输入名字')
age  = input('输入年龄')
print('My name is %s,my age is %s.'%(name,age))

