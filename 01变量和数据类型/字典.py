'''
#字具类型dict ******
#作用：记录多个key:value值，优势足每一个值value都有其对应关系/映射关系key，而key对value有描述性的功能
#义：在{}内用逗号分隔开多个key:value元素，其中value可以是任意的数据类型，而key通常应该是字符串类型
'''

info = {'name':'仰容生','age':11}
print(info)
#简单使用
print(info['name'])
print(info['age'])

#字典和列表的区别
#列表依赖于索引
#字典依赖于键值对 #key描述性的信息

L = [ '西施','顾安','木木',[{'name':[4,5,'仰容生']},'你好丫'] ]
#      0      1     2               3

#提取仰容生
print(L[3][0]['name'][2])