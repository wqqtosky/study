## Java - Methods


Java方法是组合在一起以执行操作的语句的集合。例如，当调用`System.out.println（）`方法时，系统实际上会执行几个语句以在控制台上显示消息。
现在将学习如何创建具有或不具有返回值，调用带或不带参数的方法，并在程序设计中应用方法抽象。

1、创建方法
考虑下面的例子来解释一种方法的语法 -

**Syntax**
```java
public static int methodName(int a, int b) {
   // body
}
```
方法定义由一个方法头和一个方法体组成。
- public static - 修饰符
- int  - 返回类型
- methodName  - 方法的名称
- a，b  - 形参
- int a，int b  - 参数列表

下面的语法显示了相同的内容：
```java
modifier returnType nameOfMethod (Parameter List) {
   // method body
}
```
上面显示的语法包括 -
- modifier - 它定义了方法的访问类型，它是可选的使用。
- returnType  - 方法可能会返回一个值。
- nameOfMethod  - 这是方法名称。方法签名由方法名称和参数列表组成。
- Parameter List - 参数列表，它是方法的类型，顺序和参数数量。这些是可选的，方法可能包含零参数。
- method body - 方法体定义了方法对这些语句的作用。

2、方法调用
- 对于使用方法，应该调用它。有两种调用方法的方法，即方法返回一个值或不返回任何值（不返回值）。
- 方法调用的过程很简单。当一个程序调用一个方法时，程序控制转移到被调用的方法。这个被调用的方法然后在两种情况下将控制权返回给调用者，
 - return语句被执行。
 - 它达到了结束大括号的方法。
- 返回void的方法被认为是调用语句。让我们考虑一个例子
