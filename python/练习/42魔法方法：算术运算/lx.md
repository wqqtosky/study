01、**python2.2之后对**类和类型**进行了统一，做法就是将`int()、float()、str()、list()、tuple()`这些BIF转换为工厂函数。请问所谓的工厂函数，其实是什么原理？**

- 工厂函数，其实就是一个类对象。当调用他们的时候，事实上就是创建一个相应的实例对象。
- ```python
  # a 和 b 是工厂函数（类对象） int 的实例对象
  >>> a = int('123')
  >>> b = int('345')
  >>> a + b
  468
   ```

02、**python的鸭子类型**

- 在程序设计中，鸭子类型是动态类型的一种风格。
- 在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定的。
-

```python
# I love FishC.com!
class Duck:
    def quack(self):
        print("呱呱呱！")
    def feathers(self):
        print("这个鸭子拥有灰白灰白的羽毛。")

class Person:
    def quack(self):
        print("你才是鸭子你们全家人是鸭子！")
    def feathers(self):
        print("这个人穿着一件鸭绒大衣。")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()
```
- `in_the_forest()`函数对参数`duck`只有一个要求：**就是可以实现quack()和feathers()方法**。
- 可以看出，鸭子类型给与了python这样的动态语言以多态。但是这种多态完全由程序员来约束强制实现（文档、清晰的代码和测试），并没有语言上的约束（C++继承和虚函数）。

03、**在python中，两个字符串相加会自动拼接字符串，但遗憾的是两个字符串相减却抛出异常，因此，我们可以定义一个`Nstr`类来支持字符串相减操作：A-B，从A中去除所有B的字符串。**
- 示例：

```python
>>> a = Nstr('I love FishC.com!iiiiiiii')
>>> b = Nstr('i')
>>> a - b
'I love FshC.com!'
```
- 要实现上述功能，只需要重载**__sub__**魔法方法即可：

```python
class Nstr(str):
  def __sub__(self, other):
    return self.replace(other, '')

```
04、**移位操作符是应用于二进制操作数的，现在需要你定义一个新的类`Nstr`，也支持移位操作符的运算。**
- 示例：

```python
>>> a = Nstr('I love FishC.com!')
>>> a << 3
'ove FishC.com!I l'
>>> a >> 3
'om!I love FishC.c'

```
- 要实现上述功能，只需要重载**__lshift__和__rlift__**魔法方法即可：

```python
class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]
```
05、**定义一个类`Nstr`，当该类的实例对象间发生加、减、乘、除运算时，将该对象的所有字符串对应的ASCII码之和进行计算**：

- 示例：

```python
>>> a = Nstr('FishC')
>>> b = Nstr('love')
>>> a + b
899
>>> a - b
23
>>> a * b
201918
>>> a / b
1.052511415525114
>>> a // b
1

```
方法1：
```python
class Nstr:
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误！")
    #重载下列魔法方法
    def __add__(self, other):
        return self.total + other.total
    def __sub__(self, other):
        return self.total - other.total
    def __mul__(self, other):
        return self.total * other.total
    def __truediv__(self, other):
        return self.total / other.total
    def __floordiv__(self, other):
        return self.total // other.total

```
方法2：
```python
class Nstr(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)

```
