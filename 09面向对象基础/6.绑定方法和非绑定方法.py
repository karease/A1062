#self绑定给对象方法
#简单来说就是对象在调用方法的时候会自动把该对象传入
#该方法的参数一般我们用self表示

#self绑定给都对象方法
# class A:
#
#     def f(self,n):
#         print(self,n)
#         print('我是self的方法')
#
# a = A()
# a1 = A()
# print(a)
# print('==================')
# #是哪个对象调用self参数的方法  那么传入的self就是那个对象
# a.f(1)
# print(a1)
# print('==================')
# print(a1)
#
# #类调用必须传入对象  不会自动传入对象  子弟动手传入对象
# print('************************')
# A.f(a,1)
# A.f(a1,2)


#绑定类的方法
# class B:
#     @classmethod
#     def f(cls,n):#cls是一个规范，代表是绑定类的方法
#         print(cls,n)
#         print('我是绑定类的方法')

# print(B)
# print('===================')
# B.f(1)
# #一般不这样用  绑定给类的方法给对象用
# b = B()
# print(b)
# b.f(1)




#非绑定方法/静态方法
class C:
    def f(n):
        print(n)
        print('我是非绑定方法/静态方法')
##纯粹的函数  不会自动传入类
C.f(2)
c = C()
##纯粹的函数  不会自动传入对象
C.f(3)

#总结
