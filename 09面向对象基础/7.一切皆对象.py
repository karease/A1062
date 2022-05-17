#在python中统一了类与类型的概念
class Foo:
    def find(self):
        print('我是绑定对象的方法')
#<class '__main__.Foo'>
print(Foo)
obj = Foo()
#<__main__.Foo object at 0x000001F7B83BEBC8>
print(obj)
obj.find()
#obj的类型是Foo，obj的类也是Foo
print(type(obj))
#ctrl按住不动
print(str)
#其实python在'dahai'前加了一个str类
name = str('dahai')
print(name)

#面向对象的理解  ：str这个类实例化生成了name这个对象
#dahai这个值赋值给name这个变量
print(type(name))

#面向对象的理解：name对象的方法
#数据类型的方法
print(name.startswith('d'))

obj.find()
