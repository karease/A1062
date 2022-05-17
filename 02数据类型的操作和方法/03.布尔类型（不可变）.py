'''
#布尔类型:bool  *****
#作用:用来作为判断的条件去用
#布尔值，一个True一个False
#计算机俗称电脑，即我们编写程序让计算机运行时，
应该是让计算机无限接近人脑，或者说人脑能干什么，
计算机就应该能干什么，
# 人脑的主要作用是数据运行与逻辑运算，此处的布尔类型就模拟人的逻辑运行，
即判断一个条件成立时，用True标识，不成立则用False标识
'''

# tag = False
# print(tag)
# print(type(tag))

# 重点知识
# 不仅仅是真假 还是有True 无False
# 所有的数据类型都自带布尔值
# 1.None,0,空(空字符串，空列表，空字典,)三种情况下布尔值为False,
# 2.其余均为真

tag1 = ['name','dahai']
# print(type(tag1))
# print(bool(tag1))
# True满足  False不满足
# if 如果
if tag1:
    print('数据类型自带True')
else:
    print('数据类型自带False')