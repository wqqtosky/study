## java的对象和类
1、 java是一种面向对象的语言。 作为具有面向对象功能的语言，Java支持以下基本概念

- 多态性、继承、封装、抽象化、**类、对象**、实例、方法、消息解析
- 对象 ：对象具有状态和行为。 例如：狗有状态 ：颜色，名称，品种；行为： 摇尾巴，吠叫，吃东西。
**一个对象是一个类的实例**。
- 类 ：一个类可以被定义为描述类型对象支持的行为/状态的模板或蓝图。

2、 一个类可以包含以下任何变量类型。
- 局部变量： 在方法，构造函数或块内定义的变量被称为局部变量。 该变量将在方法中声明和初始化，并且该方法完成后变量将被销毁。
- 实例变量：实例变量是类中的变量，但不包括任何方法。 这些变量在类实例化时被初始化。 实例变量可以**从该特定类的任何方法，构造器或块内部访问**。
- 类变量 ：类变量是使用static关键字在任何方法之外的类中声明的变量。

3、构造函数
- 类的子课题之一是构造函数。 每个类都有一个构造函数。 如果我们没有明确地写一个类的构造函数，那么Java编译器会为这个类构建一个默认的构造函数。
- 每次创建一个新对象时，都会调用至少一个构造函数。 构造函数的主要规则是它们应该与类具有相同的名称。 一个类可以有多个构造函数。

4、创建一个对象：一个对象是从一个类创建的。 在Java中，新关键字用于创建新对象。
从类创建对象时有三个步骤：
- 声明 ：带有变量名称和对象类型的变量声明。
- 实例化：'new'关键字用于创建对象。
- 初始化： “新”关键字后面是对构造函数的调用。 此调用将初始化新对象。
- 示例如下：
```java
public class Puppy {
   public Puppy(String name) {
      // This constructor has one parameter, name.
      System.out.println("Passed Name is :" + name );
   }

   public static void main(String []args) {
      // Following statement would create an object myPuppy
      Puppy myPuppy = new Puppy( "tommy" );
   }
}
```

5、访问实例变量和方法：实例变量和方法通过创建的对象进行访问。 要访问实例变量，以下是完全限定的路径：
  ```java
  /* First create an object */
  ObjectReference = new Constructor();

  /* Now call a variable as follows */
  ObjectReference.variableName;

  /* Now you can call a class method as follows */
  ObjectReference.MethodName();
  ```

6、**源文件声明规则**
>作为本节的最后一部分，现在让我们看看源文件声明规则。在源文件中声明类，导入语句和包语句时，这些规则至关重要。

- 每个源文件只能有一个公共类。
- 源文件可以有多个非公共类。
- **公共类名应该是源文件的名称**，并且最后应该由.java附加。例如：类名是公共类Employee {}，那么源文件应该是Employee.java。
- 如果类是在包内定义的，那么包语句应该是源文件中的第一条语句。
- 如果存在import语句，那么它们必须写在package语句和class声明之间。如果没有包语句，那么导入语句应该是源文件中的第一行。
- 导入和打包语句将暗示源文件中存在的所有类。无法向源文件中的不同类声明不同的导入或包语句。

7、Java包：简而言之，它是**对类和接口进行分类**的一种方式。
- 在Java中开发应用程序时，将会编写数百个类和接口，因此对这些类进行分类是必须的，并且使生活变得更容易。

8、引入申明：
在Java中，如果给出了包含程序包和类名称的完全限定名称，那么编译器可以轻松找到源代码或类。 引入申明是为编译器提供适当位置以找到特定类的一种方式。
例如，以下行会要求编译器加载目录`java_installation / java / io`中的所有可用类
```java
import java.io.*;
```

9、一个简单的案例
>对于我们的案例研究，我们将创建两个类。 他们是Employee和EmployeeTest。
首先打开记事本并添加下面的代码。 记住这是Employee类，而且是公共类。 现在，保存这个名字为Employee.java的源文件。
Employee类有四个实例变量：名称，年龄，职称和薪水。 该类有一个明确定义的构造函数，它带有一个参数。

```java
import java.io.*;
public class Employee {

   String name;
   int age;
   String designation;
   double salary;

   // This is the constructor of the class Employee
   public Employee(String name) {
      this.name = name;
   }

   // Assign the age of the Employee  to the variable age.
   public void empAge(int empAge) {
      age = empAge;
   }

   /* Assign the designation to the variable designation.*/
   public void empDesignation(String empDesig) {
      designation = empDesig;
   }

   /* Assign the salary to the variable	salary.*/
   public void empSalary(double empSalary) {
      salary = empSalary;
   }

   /* Print the Employee details */
   public void printEmployee() {
      System.out.println("Name:"+ name );
      System.out.println("Age:" + age );
      System.out.println("Designation:" + designation );
      System.out.println("Salary:" + salary);
   }
}
```
>正如本教程前面提到的，处理从主方法开始。 因此，为了让我们运行这个Employee类，应该有一个主方法，并且应该创建对象。 我们将为这些任务创建一个单独的类。
>以下是EmployeeTest类，它创建Employee类的两个实例，并调用每个对象的方法为每个变量分配值。
>将以下代码保存在EmployeeTest.java文件中。

```java
import java.io.*;
public class EmployeeTest {

   public static void main(String args[]) {
      /* Create two objects using constructor */
      Employee empOne = new Employee("James Smith");
      Employee empTwo = new Employee("Mary Anne");

      // Invoking methods for each object created
      empOne.empAge(26);
      empOne.empDesignation("Senior Software Engineer");
      empOne.empSalary(1000);
      empOne.printEmployee();

      empTwo.empAge(21);
      empTwo.empDesignation("Software Engineer");
      empTwo.empSalary(500);
      empTwo.printEmployee();
   }
}
```
