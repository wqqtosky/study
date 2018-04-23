## java的基础语法
1、java 介绍
- **当我们考虑Java程序时，它可以被定义为通过调用彼此的方法进行通信的对象的集合**。现在让我们简单地看一下类，对象，方法和实例变量的含义。
- **对象** - 对象具有状态和行为。例如：狗有状态 - 颜色，名称，品种以及行为，如摇尾巴，吠叫，吃东西。一个对象是一个类的实例。
- **类**： 一个类可以被定义为一个模板/蓝图，描述该类型的对象支持的行为/状态。
- **方法**： 一种方法基本上是一种行为。一个类可以包含许多方法。它是在写逻辑的方法中，操纵数据并执行所有操作。
- **实例变量**： 每个对象都有其独特的一组实例变量。对象的状态由分配给这些实例变量的值创建。

2、java 代码
- 编译：`C:\> javac MyFirstJavaProgram.java`
- 执行：`C:\> java MyFirstJavaProgram `

3、基本语法
> 关于Java程序，请记住以下几点非常重要。

- 区分大小写：Java区分大小写，这意味着标识符Hello和hello在Java中会有不同的含义。
- class名称：对于所有class，首字母应采用大写字母。如果用几个单词形成class名称，每个内部单词的第一个字母应该是大写字母。
>示例：class MyFirstJavaClass
- 方法名称：所有方法名称应以小写字母开头。如果用几个单词来形成方法的名称，那么每个内部单词的第一个字母应该是大写字母。
>示例：public void myMethodName（）
- 程序文件名：**程序文件的名称应该与类名完全一致**。保存文件时，应使用类名（请记住Java区分大小写）并在名称末尾附加'**.java**'（如果文件名和类名不匹配，则程序不会编译）。
>例如：假设'MyFirstJavaProgram'是类名。然后该文件应该保存为'MyFirstJavaProgram.java'
- public static void main（String args []）： Java程序处理从main（）方法开始，该方法是每个Java程序的强制性部分。

3、java 标识符
>所有Java组件都需要名称。用于类，变量和方法的名称称为标识符。

- 在Java中，关于标识符有几点要记住。他们如下所有标识符应以字母（A到Z或a到z），货币字符（$）或下划线（_）开头。在第一个字符之后，标识符可以具有任何字符组合。
- 关键词不能用作标识符。
- 标识符区分大小写。
>合法标识符的例子：age，$salary，_value，__1_value。
>非法标识符的例子：123abc，-salary。

4、Java修饰符
>像其他语言一样，可以使用修饰符来修改类，方法等。有两类修饰符：

- 访问修饰符 ：default, public , protected, private
- 非访问修饰符：final，abstract，strictfp

5、java 变量
- 局部变量
- 类变量（静态变量）
- 实例变量（非静态变量）

6、Java枚举
- 枚举是在Java 5.0中引入的。枚举限制一个变量只有一个预定义的值。此枚举列表中的值称为枚举。
通过使用枚举，可以减少代码中的错误数量。
- 例如，如果我们考虑新鲜果汁店的应用程序，则可以将玻璃尺寸限制为小，中，大。这将确保它不允许任何人订购除小型，中型或大型以外的任何尺寸。

```java
class FreshJuice {
   enum FreshJuiceSize{ SMALL, MEDIUM, LARGE }
   FreshJuiceSize size;
}

public class FreshJuiceTest {

   public static void main(String args[]) {
      FreshJuice juice = new FreshJuice();
      juice.size = FreshJuice.FreshJuiceSize.MEDIUM ;
      System.out.println("Size: " + juice.size);
   }
}
```
7、Java 关键词
>以下列表显示了Java中的保留字。这些保留字不能用作常量或变量或任何其他标识符名称。

abstract| assert  |  boolean |  break | byte | case
--|---|---|---|---|--
catch| char  |  class |  const | continue | default
do  | double| else|  enum  | extends  |  final
float  |   |   |   |   |

8、接口
- 在Java语言中，可以将**接口定义为对象之间如何相互通信的契约**。当涉及到继承的概念时，接口起着至关重要的作用。
- 接口定义了派生类（子类）应该使用的方法。但是这些方法的实现完全取决于子类。
