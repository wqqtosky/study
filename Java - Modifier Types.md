## java 修饰符
修饰符是添加到这些定义以更改其含义的关键字。 Java语言具有各种各样的修饰符，包括以下两种：
访问修饰符、非访问修饰符。

### 访问修饰符：
java提供了许多访问修饰符来**为类，变量，方法和构造函数设置访问级别**。 四个访问级分别是：
- 对包可见（默认）。 不需要修饰符。
- 仅对类可见（私有）。
- 对包和所有子类可见（受保护）。
- 对所有的可见（公共）。

1、默认访问修饰符 - 无关键字

默认访问修饰符意味着我们不明确为类，字段，方法等声明访问修饰符。
没有任何访问控制修饰符的变量或方法可用于同一包中的任何其他类。 接口中的字段隐式地为`public static final`，接口中的方法默认为`public`。
- 可以在没有任何修饰符的情况下声明变量和方法，如下例所示：

```java
tring version = "1.5.1";

boolean processOrder() {
   return true;
}
```
2、私有访问修饰符 - 私有

- 被声明为private的方法，变量和构造函数只能在声明的类本身内访问。
- **私有访问修饰符是最严格的访问级别。 类和接口不能是私有的。**
- 如果类中存在公共`getter`方法，则可以在类外部访问声明为`private`的变量。
- 使用私有修饰符是**对象封装自身并隐藏外部数据**的主要方式。
- 例如：
```java
public class Logger {
   private String format;

   public String getFormat() {
      return this.format;
   }

   public void setFormat(String format) {
      this.format = format;
   }
}
```
- 在上例中，Logger类的`format`变量是私有的，所以其他类无法直接检索或设置其值。
因此，为了让这个变量对外界可用，我们定义了两个公共方法：`getFormat（）`，它返回`format`的值; `setFormat（String）`，它设置`format`的值。

3、受保护的访问修饰符 - 受保护
- 在父类中声明受保护的变量，方法和构造函数只能由其他包的子类或受保护成员类的包中的任何类访问。
- **受保护的访问修饰符不能应用于类和接口**。方法，字段可以声明为受保护的，但是接口中的方法和字段不能声明为受保护的。
- 受保护的访问使子类有机会使用辅助方法或变量，同时防止不相关的类尝试使用它。
- 以下父类使用受保护的访问控制，以允许其子类覆盖openSpeaker（）方法 ：

```java
class AudioPlayer {
   protected boolean openSpeaker(Speaker sp) {
      // implementation details
   }
}

class StreamingAudioPlayer {
   boolean openSpeaker(Speaker sp) {
      // implementation details
   }
}
```
- 上例中，如果我们将`openSpeaker（）`方法定义为私有的，那么它将不能从`AudioPlayer`以外的任何其他类访问。如果我们把它定义为公开的话，那么它就可以被所有的外部世界所接受。但是我们的意图是只将这个方法暴露给它的子类，这就是为什么我们使用了`protected`修饰符。

4、公共访问修饰符 - 公共
- 可以从任何其他类访问公开的类，方法，构造函数，接口等。因此，可以从属于Java Universe的任何类访问在公共类中声明的字段，方法和块。
- 但是，如果我们试图访问的公共类位于不同的包中，那么公共类仍然需要导入。由于类继承，类的所有公共方法和变量都由其子类继承。
- 例如：应用程序的main（）方法必须是公共的。否则，Java解释器（如Java）无法调用它来运行该类。
```java
public static void main(String[] arguments) {
   // ...
}
```
5、访问控制和继承

继承方法按以下规则被执行：
- 在父类中公开的方法也必须在所有子类中公开。
- 在父类中声明受保护的方法在子类中必须受保护或公开;他们不能是私有的。
- 私有的方法根本不会被继承，所以对它们没有规则。

### 非访问修饰符
Java提供了许多非访问修饰符来实现许多其他功能。
- 用于创建类方法和变量的**静态修饰符**。
- 用于完成类，方法和变量实现的**final修饰符**。
- 创建抽象类和方法的**抽象修饰符**。
- **synchronized和volatile修饰符**，用于线程。

1、静态修饰符

1.1 静态变量
- static关键字用于创建独立存在于为该类创建任何实例的变量。不管类的实例数量有多少，只存在一个静态变量副本。
- **静态变量也称为类变量。局部变量不能被声明为静态的。**

1.2 静态方法
- static关键字用于创建独立存在于为该类创建任何实例的方法。
- 静态方法不使用任何它们在其中定义的类的任何对象的实例变量。静态方法从参数中获取所有数据，并从这些参数计算某些内容，而不参考变量。
- **类变量和方法可以使用类名后面跟一个点和变量或方法的名称来访问**。
- 静态修饰符用于创建类方法和变量，如下例所示：
```java
public class InstanceCounter {

   private static int numInstances = 0;

   protected static int getCount() {
      return numInstances;
   }

   private static void addInstance() {
      numInstances++;
   }

   InstanceCounter() {
      InstanceCounter.addInstance(); //访问类方法
   }

   public static void main(String[] arguments) {
      System.out.println("Starting with " + InstanceCounter.getCount() + " instances");

      for (int i = 0; i < 500; ++i) {
         new InstanceCounter();
      }
      System.out.println("Created " + InstanceCounter.getCount() + " instances");
   }
}
```
Output：
```java
Started with 0 instances
Created 500 instances
```

2、final修饰符

2.1 final变量
- final变量只能被显式初始化一次。声明为final的引用变量永远不能被重新分配以引用不同的对象。
- 对象内的数据可以更改。所以，对象的状态可以改变，但不能作为引用。
- 通过变量，final修饰符通常与静态static一起使用，以使常量成为类变量。
- 示例：
```java
public class Test {
   final int value = 10;

   // The following are examples of declaring constants:
   public static final int BOXWIDTH = 6;//常量（类变量）
   static final String TITLE = "Manager";

   public void changeValue() {
      value = 12;   // will give an error
   }
}
```

2.2 final方法
- **final方法不能被任何子类覆盖**。如前所述，final修饰符可以防止在子类中修改方法。
- 使用final方法的主要目的是该方法的内容不应该被任何局外人所改变。
- 类中使用final修饰符声明的方法，如下例所示：
```java
public class Test {
   public final void changeName() {
      // body of method
   }
}
```
2.3 final类
- 使用被声明为final的类的主要目的是为了防止该类被分类。如果一个类被标记为final，那么没有类可以继承该类的任何特性。
- 示例：
```java
public final class Test {
   // body of class
}
```

3、抽象修饰符

3.1抽象类

- 抽象类永远不能实例化。如果一个类被声明为抽象的，那么唯一的目的是扩展这个类。
- 一个类不能既抽象又final（因为final的类不能被扩展）。如果一个类包含抽象方法，那么该类应该被声明为抽象的。否则，将会抛出一个编译错误。
- 抽象类可能包含抽象方法和普通方法。
