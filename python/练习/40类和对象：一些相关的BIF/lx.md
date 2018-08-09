01、**如何判断一个类是否为另一个类的子类？**

- 使用`issubclass(class,classinfo)` 函数，如果第一个参数(class)是第二个参数(classinfo)的一个子类，则返回true，否则返回false。
- 一个类被认为是其自身的子类。
- `classinfo`可以是类对象组成的元组，只要class为其中任何一个候选类的子类，则返回true。


02、**如何判断对象a是否为类A的实例对象？**

- 使用`isinstance(object,classinfo)`函数，如果第一个参数（object）是第二个参数(classinfo)的实例对象，则返回true，否则返回false。
- 如果object是classinfo的子类的一个实例，也符合条件。
- 如果第一个参数不是对象，则永远返回false。
- classinfo是类对象组成的元组，只要class为其中任何一个候选类的子类，则返回true。

03、**如何优雅的避免访问对象不存在的属性（不产生异常）？**

2种方法：

方法1：使用`hasattr(object,name)`函数判断属性是否存在，如果存在再访问。（object是对象，name是属性名的字符串形式）

方法2：使用`getattr(object,name[,default])`函数并设置default参数，如果指定的属性不存在，返回default的值。（object是对象，name是属性名的字符串形式）
