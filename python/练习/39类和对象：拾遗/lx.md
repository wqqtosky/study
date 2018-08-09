01、**什么是组合？**
-  python的继承机制很有用，很容易把代码复杂化以及依赖隐含继承。因此，我们经常使用**组合来代替继承**。在python里组合其实很简单，直接在类定义中把需要的类放进去实例化就可以了。
- 例子：

```python
//乌龟类
class Turtle:
    def __init__(self,x):
        self.num = x
//鱼类
class Fish:
    def __init__(self,x):
        self.num = x
//水池类
class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)   #组合乌龟类进来，直接把需要的类实例化，实例化出来一个乌龟
        self.fish = Fish(y)       #组合鱼类进来

    def print_num(self):
        print("水池里总共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num,self.fish.num))

pool = Pool(1,10)
pool.print_num()

```
02、**什么时候用组合，什么时候用继承？**

- 根据实际应用场景确定。简单的说，组合用于**“有一个”**的场景中，继承用于**“是一个”**的场景中。例如，水池里有一个乌龟，天上有一只鸟，这些适合用组合；青瓜是瓜，鲨鱼是鱼，这些就该用继承。

03、**类对象什么时候产生的？**

-  当这个类定义完的时候，类定义就变成类对象，可以直接通过“类名.属性”或者“类名.方法名()”引用或使用相关的属性或方法。

04、**如果对象的属性跟方法名相同，会怎样？**

- 属性会覆盖方法。

05、**定义一个栈类，用于模拟后进先出（LIFO）特性的数据结构。主要有以下方法：**

方法名  | 含义
--|--
isEmpty()  |  判断当前栈是否为空（返回true或false）
  push()|  网栈的顶部压入一个数据项
  pop()|从栈顶弹出一个数据项，并在栈中删除
top()  |  显示当前栈顶的一个数据项
bottom()  |  显示当前栈底的一个数据项

代码如下：
```python
class Stack:
  def __init__(self,start=[]):
    self.stack = []
    for x in start:
      self.push(x)
  def isEmpty(self):
    return not self.stack
  def push(self,obj):
    self.stack.append(obj)
  def pop(self):
    if not self.stack:
      print('警告：栈为空！')
    else:
      return self.stack.pop()
  def top(self):
    if not self.stack:
      print('警告：栈为空！')
    else:
      return self.stack[-1]
  def bottom(self):
    if not self.stack:
      print('警告：栈为空！')
    else:
      return self.stack[0]
```
