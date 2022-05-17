# print('my name is "yrs".')
# print("my name is 'yrs'.")
#
# name4 = 'abcdef'
# #        012345
# #索引从0开始，现实中书本从1开始
# #取出第一个英文字符
# print(name4[0])
# print(name4[1])
# print(name4[5])
# print(name4[-1])
# print(name4)
#
# name5='仰容生'
# print(name5[0])

#字符串相加
# print('yrs'+'ssss')
# print('yrs'*10)

#提取单个字符
# msg = 'hello world'
#      0123456789十
# print(msg[0])
# print(msg[1])
#提取多个字符
#2.切片 （顾头不顾尾 ， 步长）查找字符串当中的一段值 [起始值 : 终止值 : 步长]
#相当于切黄瓜， 一节一节

# msg  = 'hello world'
#步长默认是1
# print(msg[0:5])
# print(msg[0:5:1])
# print(msg[0:5:2])
# #提取不改变原值
# print(msg)
#
# #了解
# print(msg[::-1])#可倒置输出
# print(msg[10:5:-1])

#3长度len方法 可以计算长度

# print(len(msg))

#4成员运算in 和not in ：判断一个子字符串是否存在于一个大的字符串中
#返回布尔型 True False

# print('yrs' in 'My name is yrs.')
# print('yrs' not in 'My name is yrs.')
# print('asd' not in 'My name is yrs.')

#字符串的方法
#增
#字符串拼接
#这是一个字符串
# print('yrs'+'aaa')
# #这是2个字符串 一行打印
# print('yrs','aaa')
#

#format
# print('my name is {}'.format('yrs'))
# print('my name is {},my age is {}'.format('yrs',11))
# print('my name is {0},my age is {1}'.format('yrs',11))
# print('my name is {1},my age is {0}'.format('yrs',11))

#join(把列表里的字符串 拼接起来)
# str1 = '真正的勇士'
# str2 = '敢于直面惨淡的人生'
# str3 = '敢于正视淋漓的鲜血'
# list1 = [str1,str2,str3]
# print(list1)
# #可以把列表里的元素组合成字符串
# print(''.join(list1))
# print(','.join(list1))
# print('***'.join(list1))

#删
# name = 'yrs'
# del name
# print(name)

#改
#1 字符串的字母全部变成大写或小写 lower upper
#不可变类型
# msg1 = 'abC'
# print(msg1)
# print(id(msg1))
#
# #msg1.lower() 它会产生一个新值 这个值是变的
# msg2 = msg1.lower()
#
# print(msg1)
# print(id(msg1))
#
# print(msg2)
# print(id(msg2))

#字符串是不可变类型
#不可变类型   值变 id也变

#字符串进行改变需要重新赋值，所以它也是不可变类型，它的原值的变量不会变
#只是做了一个方法改变了它的值，重新赋值给一个新的变量

#2把第一个字母转换成大写capitalize

# letter = 'abcd'
# letter1 = letter.capitalize()
# #原值
# print(letter)
# #新值
# print(letter1)

#字符串切分成列表 split 默认空格字符切分
# msgg = 'hello world python'
# a = msgg.split()
# print(a)#  ['hello', 'world', 'python']
# print(msgg)#  hello world python

# msgg = 'hello*world*python'
# a = msgg.split('*')
# print(a)
#切分split的作用：针对按照某种分隔符组织的字符串，可以用split将其切分成列表，从而进行取值
# msggg = 'root:123456'
# #        01234
# print(msggg[0:4])
# print(msggg.split(':')[0])
# print(msggg.split(':')[1])

#替换replace（存在的字符，新的字符，个数）
# msggg = 'yrs你好'
# #默认是所有
# print(msggg.replace('你','我'))
# print(msggg.replace('y','a'))
# #指定个数
# print(msggg.replace('y','a',1))

#5 去掉字符串左右两边的字符 strip不写默认是空格字符 不管中间其它的字符
# user = '                 us  er            '
# print(user)
# print(user.strip())


#center,ljust,rjust 多余添加自己想要的字符
#yrs放中间，   *补充  整体11个字符
# print('yrs'.center(11,'*'))
# #l 放左边  r 放右边
# print('yrs'.ljust(11,'*'))
# print('yrs'.rjust(11,'*'))

#1、find ， index
#查找子字符串在大字符串的哪个位置（起始索引）
# msga = 'hello dahai is dsb dahai'
# print(msga.find('dahai'))
# #没找到会返回-1
# print(msga.find('aaaaaaaaa'))
#
# print(msga.index('dahai'))
# #没找到会报错
# print(msga.index('aaaaaaaaa'))

# msga = 'hello dahai is dsb dahai'
# #统计一个子字符串在大字符串中出现的次数 count
# print(msga.count('dahai'))

# 判断一个字符串里的数据是不是都是数字 isdigit # 返回布尔值
# mun = '1818'
# muna = 'a1818'
# print(mun.isdigit())
# print(muna.isdigit())

# 判断每个字符是不是都是字母 isalpha
# mun2 = 'aaa'
# mun3 = '22aaa'
# print(mun2.isalpha())
# print(mun3.isalpha())


# 字符串里面全是数字  是可以转换乘整型
# n = '111'
# n1 = '11aaa'
# print(type(n))
# print(n)
# # # 可以变成真正的数字
# print(type(int(n)))
# print(int(n))
# # # 不能转  必须要字符串里面全是数字
# int(n1)


# 比较开头的元素是否相同 startswith
# 比较结尾的元素是否相同 endswith
#T F
# mm = 'dahai xialuo'
# print(mm.startswith('dahai'))
# print(mm.startswith('d'))
# print(mm.startswith('da'))
# print(mm.startswith('a'))
# print(mm.endswith('o'))
# print(mm.endswith('luo'))
# print(mm.endswith('xialuo'))


# 判断字符串中的值是否全是小写的 islower
# 判断字符串中的值是否全是大写的 isupper
# letter2 = 'ABC'
# letter3 = 'abc'
# letter4 = 'aABC'
# #T F
# print(letter2.isupper())
# print(letter2.islower())
# print(letter3.isupper())
# print(letter3.islower())
# print(letter4.isupper())
# print(letter4.islower())


# 字符串的转义
# 字符串的转义   加了 \  字符不再表示它本身的含义
# 常用的  \n  \t
# \n 竖向换行符
# print('hello\npython')
# # # \t 横向换行符 相当于一个tab
# print('hello\tpython')

# # 反转义
# # 第一种  加了 \  字符不再表示它本身的含义 每个都要加  \
#print('hello\\npython')
# print('hello\\npython hello\\tpython')

# 第二种  加了 r  字符不再表示它本身的含义  只要在前面写一次
# print(r'hello\npython hello\tpython')

# 不可变 不能强行改它的原值
# 所有的方法全是产生了新值
# msg = 'hello world'

# msg[0] = 'w'
