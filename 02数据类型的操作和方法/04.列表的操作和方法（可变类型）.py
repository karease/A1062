# 字符串，数字，布尔，复数 都是一个值(不同的数据类型)
'''
# 列表类型：list  *****
#作用：记录/存多个值，可以方便地取出来指定位置的值，比如人的多个爱好，一堆学生姓名
#定义：在[]内用逗号分隔开多个任意类型的值
'''

# L = ['大海',1,1.2,[1.22,'小海']]
#
# print(L)
# L[0] = '红海'
# print(L)

# 值修改，id变    是     不可变类型
# 一个值 字符串，数字，布尔，复数 不可变类型

# 值修改，id不变是可变类型
# 列表是可变类型
# 多个值容器 有序的      列表  可变类型

# 查
# 2、切片(顾头不顾尾，步长)
# 查找列表当中的一段值 [起始值:终止值:步长]
# 和字符串提取字符一样,只不过字符串取的是字符，列表取的是一个数据类型/元素

# name = 'dahai'
# print(name[0])
# # 但是字符串不能索引改值     不可变类型
# name[0] = 'fff'

L = ['dahai',1,1.2,[1.22,'小海']]
#     0      1  2   3
print(L[0:3])
print(L[0:3:1])
print(L[0:3:2])