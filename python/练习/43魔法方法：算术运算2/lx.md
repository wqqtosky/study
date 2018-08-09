01、**python 什么时候会用到反运算的魔法方法？**

- 例如`a+b`，如果 a对象的__add__方法没有实现或者不支持相应的操作，那么python就会自动调用b的__radd__方法。

02、**请问如何在继承的类中调用基类的方法？**

- 使用`super()`这个BIF函数。

```python
class Derived(Base):
    def meth (self):
        super(Derived, self).meth()
```

03、**如果我要继承的基类是动态的（有时候是A，有时候是B），应该如何部署我的代码，以便基类可以随意改变？**
- 可以先定义一个别名，在类定义的时候，使用别名代替你要继承的基类。
- 当你想要改变基类的时候，只要修改给别名赋值的那个语句即可。
- 这种方法适合在资源视情况而定的时候。
- 示例：

```python
BaseAlias = BaseClass  # 为基类取别名

class Derived(BaseAlias):
    def meth(self):
        BaseAlias.meth(self)  # 通过别名访问基类
        ...
```
04、**如何使用类的静态属性？**

- 类的静态属性就是在类中直接定义的变量（**没有self.**）。引用类的静态属性使用**“类名.属性名”**的形式。
- 类的静态属性应用（计算该类被实例化的次数）：

```python
class C:
    count = 0  # 静态属性

    def __init__(self):
        C.count = C.count + 1  # 类名.属性名的形式引用

    def getCount(self):
        return C.count
```
05、**举例说明如何使用类的静态方法，并指出使用类的静态方法有什么需要注意的地方？**
- 静态方法是类的特殊方法，静态方法只需要在普通方法的前边加上**@staticmethod**修饰符即可。

```python
class C:
        @staticmethod  # 该修饰符表示 static() 是静态方法
        def static(arg1, arg2, arg3):
                print(arg1, arg2, arg3, arg1 + arg2 + arg3)

        def nostatic(self):
                print("I'm the f**king normal method!")
```

- 静态方法最大的优点：**不会绑定到实例对象上**，换而言之就是节省开销。

```python
>>> c1 = C()
>>> c2 = C()
# 静态方法只在内存中生成一个，节省开销
>>> c1.static is C.static
True
>>> c1.nostatic is C.nostatic
False
>>> c1.static
<function C.static at 0x03001420>
>>> c2.static
<function C.static at 0x03001420>
>>> C.static
<function C.static at 0x03001420>
# 普通方法每个实例对象都拥有独立的一个，开销较大
>>> c1.nostatic
<bound method C.nostatic of <__main__.C object at 0x03010590>>
>>> c2.nostatic
<bound method C.nostatic of <__main__.C object at 0x032809D0>>
>>> C.nostatic
<function C.nostatic at 0x0328D2B8>

```
- 使用的时候需要注意的地方：**静态方法不需要self参数，因此即使是使用对象去访问，self参数也不会传进去**。

```python
>>> c1.static(1, 2, 3)
1 2 3 6
>>> C.static(1, 2, 3)
1 2 3 6
```
06、定义一个类，当实例化该类时，自动判断传入了多少个参数，并显示出来。

```python
class C:
    def __init__(self, *args):
      if not args:
        print("并没有传入参数")
      else:
        print("传入了 %d 个参数，分别是：" % len(args), end='')
        for each in args:
          print(each, end=' ')

```
07、**定义一个单词（`Word`）类继承自字符串，重写比较操作符，当两个`Word`类对象进行比较时，根据单词的长度进行比较大小。**

_加分项：实例化时，如果传入的是带空格的字符串，则取第一个空格前的单词作为参数。_
- 加分项可以通过重载__new__方法来实现（因为字符串是不可变类型），通过重写__gt__、__lt__、__ge__、__le__方法来定义Word类在比较操作中的表现。

```python
'''存储单词的类，定义比较单词的几种方法'''
class Word(str):
    def __new__(cls, word):
        # 注意我们必须要用到 __new__ 方法，因为 str 是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] #word是第一个空格之前的所有字符
        return str.__new__(cls, word)
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
```
