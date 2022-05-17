'''

'''

class G():
    x='G'
    pass

class E(G):
    x='E'
    pass
class F(G):
    x='F'
    pass

class B(E):
    x='B'
    pass
class C(F):
    x='C'
    pass
class D(G):
    x='D'
    pass

class A(B,C,D):
    x = 'A'
    pass

obj = A()
print(obj.x)

#python专门为继承类内置了一个mro方法  用来查看c3算法的计算结果
print(A.mro())