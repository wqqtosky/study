## Java 变量类型
1、变量为我们提供了程序可以操作的命名存储空间。 Java中的每个变量都有一个特定的类型，它决定了变量**内存的大小和布局**;可以存储在该存储器中的值的范围;以及可以应用于该变量的一组操作。
必须先声明所有变量，然后才能使用它们。以下是变量声明的基本形式：
- data type variable [ = value][, variable [ = value] ...] ;

2、为了定义特定变量类型大于一个的变量，可以使用逗号分隔列表的形式表示：
```java
int a, b, c;         // Declares three ints, a, b, and c.
int a = 10, b = 10;  // Example of initialization
byte B = 22;         // initializes a byte type variable B.
double pi = 3.14159; // declares and assigns a value of PI.
char a = 'a';        // the char variable a iis initialized with value 'a'
```
3、Java语言中可用的各种变量类型有三种：**局部变量、实例变量、类/静态变量**。

4、局部变量：
- 局部变量在方法，构造函数或块中声明。
- 在方法，构造函数或块被调用时会创建局部变量，并且一旦变量退出方法，构造函数或块，该变量就会被销毁。
- **访问修饰符不能用于局部变量**。
- 局部变量只在声明的方法，构造函数或块中可见。
- 局部变量在内部**以堆栈级别**实现。
- 局部变量没有默认值，因此应**声明局部变量并在首次使用之前分配初始值**。

5、实例变量：
- **实例变量在类中声明**，但在方法，构造函数或任何块之外声明。
- 为堆中的对象分配空间时，将为每个实例变量值创建一个**插槽**。
- 实例变量是在使用关键字'new'创建对象时创建的，并在对象销毁时进行销毁。
- 实例变量可以在使用之前或之后在类级别中声明。
- 实例变量包含必须被多个方法，构造函数或块所引用的值，或者对象状态的基本部分必须存在整个类中。
- **访问修饰符可以用于实例变量**。
- 实例变量对类中的所有方法，构造函数和块都是可见的。通常，**建议将这些变量设为私有**。但是，**可以使用访问修饰符为这些变量提供子类的可见性**。
- 实例变量具有默认值。对于数字，默认值为0，对于布尔值是false，对于对象引用则为null。值可以在声明期间或在构造函数中分配。
- 可以通过调用类中的变量名直接访问实例变量。但是，在静态方法中（实例变量具有可访问性时），应该使用完全限定名称来调用它们。
- 示例：

```java
import java.io.*;
public class Employee {

   // this instance variable is visible for any child class.
   public String name;

   // salary  variable is visible in Employee class only.
   private double salary;

   // The name variable is assigned in the constructor.
   public Employee (String empName) {
      name = empName;
   }

   // The salary variable is assigned a value.
   public void setSalary(double empSal) {
      salary = empSal;
   }

   // This method prints the employee details.
   public void printEmp() {
      System.out.println("name  : " + name );
      System.out.println("salary :" + salary);
   }

   public static void main(String args[]) {
      Employee empOne = new Employee("Ransika");
      empOne.setSalary(1000);
      empOne.printEmp();
   }
}
```

6、类/静态变量
- 类变量（也称为静态变量）在**类中由static关键字声明，但是在方法、构造函数或块之外进行声明**。
- 无论从中创建多少个对象，每个类的每个类变量只有一个副本。
- 程序启动时会创建静态变量，程序停止时会被销毁。
- 除了声明为常量外，很少使用静态变量。常量是声明为public / private，final和static的变量。常量变量从不改变初始值。
- 静态变量存储在静态内存中。除了声明的final之外，使用静态变量很少见，并且用作公共或私有常量。
- 可见性与实例变量类似。但是，大多数静态变量都是公开的，因为它们必须可供该类的用户使用。
- 默认值与实例变量相同。对于数字，默认值为0;对于布尔来说，是false;对于对象引用，是Null。值可以在声明期间或在构造函数中分配。此外，可以在特殊的静态初始化块中分配值。
- 通过调用类名称`ClassName.VariableName`可以访问静态变量。
- **将类变量声明为`public static final`时，变量名称（常量）全部大写。如果静态变量不是public和final，则命名语法与实例和局部变量相同**。
- 示例：
```java
import java.io.*;
public class Employee {

   // salary  variable is a private static variable
   private static double salary;

   // DEPARTMENT is a constant
   public static final String DEPARTMENT = "Development ";

   public static void main(String args[]) {
      salary = 1000;
      System.out.println(DEPARTMENT + "average salary:" + salary);
   }
}
```
