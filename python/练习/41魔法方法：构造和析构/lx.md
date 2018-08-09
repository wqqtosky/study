01、**请问`__new__`方法负责什么任务？**

-  `__new__`方法返回一个实例对象，通常是参数**cls这个类**的实例化对象，当然也可以返回其他对象的实例化对象。

02、**`__del__`方法什么时候会被自动调用？**

- 当对象要被销毁的时候，这个方法就会被调用。
- 但一定要注意，并不是`del x`就相当于自动调用`x.__del__()`，`__del__()`方法是当垃圾回收机制回收这个对象的时候调用的。

03、**写一个`FileObject`类，给文件对象进行包装，从而在删除对象时文件能自动关闭。**

  - ```python
  class FileObject:
    def __init__(self,filename='sample.txt'):
      self.new_file = open(filename,'r+') #读写模式打开一个文件

    def __del__(self):
      self.new_file.close()
      del self.new_file
  ```

04、**定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度=摄氏度*+32）**
- 希望尽可能简练地实现功能，如下：
- ```python
>>> print(C2F(32))
89.6
```
为了简练的实现上述功能，采取了“偷龙转凤”的小技巧。在类进行初始化之前，通过“掉包”arg参数，让实例对象直接返回计算后的结果。
- ```python
  class C2F(float):
    "摄氏度转换为华氏度"
    def __new__(cls, arg=0.0):
      return float.__new__(cls, arg * 1.8 + 32)

  ```

05、**定义一个类继承int类型，并实现一个特殊功能：当传入的参数是字符串的时候，返回该字符串中所有字符的ASCII码的和（使用ord()获得一个字符的ASCII值）**

- ```python
  class Nint(int):
    def __new__(cls, arg=0):
      if isinstance(arg, str):
        total = 0
        for each in arg:
          total += ord(each)
        arg = total
      return int.__new__(cls, arg)
  ```
