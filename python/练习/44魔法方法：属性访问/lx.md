01、**自定义该类的属性被访问的行为，应该重写哪个魔法方法？**
- `__getattribute__(self,name)`

02、**按要求重写魔法方法：当访问一个不存在的属性时，不报错且提示“该属性不存在！”**
```python
>>> class Demo:
	def __getattr__(self,name):
		return '该属性不存在！'


>>> demo = Demo()
>>> demo.x
'该属性不存在！'
```
03、**编写Demo类，访问一个不存在的属性可以直接输出结果。**
- 重写`__getattr__`方法

```python
>>> class Demo:
	def __getattr__(self,name):
		self.name = 'FishC'
		return self.name


>>> demo = Demo()
>>> demo.x
'FishC'
```
04、**编写一个Counter类，用于实时检测对象有多少个属性。**

```python
>>> class Counter:
	def __init__(self):
		super().__setattr__('counter',0)
	def __setattr__(self,name,value):
		super().__setattr__('counter',self.counter+1)
		super().__setattr__(name,value)
	def __delattr__(self,name):
		super().__setattr__('counter',self.counter-1)
		super().__delattr__(name)

>>> c = Counter()
>>> c.x = 1
>>> c.counter
1
>>> c.y = 1
>>> c.z
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c.z
AttributeError: 'Counter' object has no attribute 'z'
>>> c.counter
2
>>> c.z = 2
>>> c.counter
3
```
