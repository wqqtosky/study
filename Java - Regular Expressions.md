## Java - 正则表达式（未完）
Java提供了用于与正则表达式进行模式匹配的**java.util.regex**包。 Java正则表达式与`Perl`编程语言非常相似，并且非常容易学习。
正则表达式是一个特殊的字符序列，可以使用模式中保存的专用语法来帮助您匹配或查找其他字符串或字符串集。它们可以用于搜索，编辑或操纵文本和数据。
`java.util.regex`包主要由以下三个类组成 ：
- `Pattern`类 - 模式对象是正则表达式的编译后的表示。 `Pattern`类不提供公共构造函数。要创建一个模式，你必须首先调用其一个`public static compile（）`方法，然后它将返回一个Pattern对象。这些方法接受一个正则表达式作为第一个参数。
- `Matcher`类 -  `Matcher`对象是解释模式并对输入字符串执行匹配操作的引擎。像`Pattern`类一样，`Matcher`没有定义公共构造函数。通过调用`Pattern`对象上的`matcher（）`方法来获得`Matcher`对象。
- `PatternSyntaxException`  -  `PatternSyntaxException`对象是指示正则表达式模式中的语法错误的未经检查的异常。

1、捕获组
- 捕获组是一种将多个角色作为单个单位对待的方式。它们是通过将字符分组在一组括号内创建的。例如，正则表达式（dog）会创建一个包含字母“d”，“o”和“g”的组。
- 捕获组通过从左至右数开括号进行编号。在表达式（（A）（B（C）））中，例如，有四个这样的组：
 - （（A）（B（C）））
 - （A）
 - （B（C））
 - （C）
- 要找出表达式中有多少个组，请在匹配器对象上调用`groupCount`方法。 `groupCount`方法返回一个`int`，显示匹配器模式中存在的捕获组的数量。
- 还有一个特殊的组，0组，它总是代表整个表达。该组不包括在由groupCount报告的总数中。
- 以下示例说明如何从给定的字母数字字符串中查找数字字符串：

```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexMatches {

   public static void main( String args[] ) {
      // String to be scanned to find the pattern.
      String line = "This order was placed for QT3000! OK?";
      String pattern = "(.*)(\\d+)(.*)";

      // Create a Pattern object
      Pattern r = Pattern.compile(pattern);

      // Now create matcher object.
      Matcher m = r.matcher(line);
      if (m.find( )) {
         System.out.println("Found value: " + m.group(0) );
         System.out.println("Found value: " + m.group(1) );
         System.out.println("Found value: " + m.group(2) );
      }else {
         System.out.println("NO MATCH");
      }
   }
}
```
