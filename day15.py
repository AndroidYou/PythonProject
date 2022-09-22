"""
 函数
 定义；
   1. 函数代码块以def关键词开头，后接函数标识符名称和圆括号()
   2. 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
   3. 函数的第一行语句可以选择性地使用文档字符串- 用于存放函数说明
   4. 函数内容以冒号 ： 起始，并且缩进
   5. return[表达式]结束函数，选择性地返回一个值给调用方，不带表达式的return相当于返回None
   6.参数： 和kotlin一样  支持默认参数，可变参数 * 修饰，参数名=“” 赋值，参数顺序可变
   7.双星号的参数  会以字典的形式传参
   8.如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：


 语法
    def 函数名（参数列表）:
    函数体

 默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的


 参数传递
 在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：

可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响


通过 id() 函数来查看内存地址变化：


匿名函数：
Python 使用 lambda 来创建匿名函数。
匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

语法
lambda 函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression

return 语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的 return 语句返回 None


强制位置参数
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。

"""


def hello():
    print("Hello Python ！")


# 比较大小
def maxNum(a, b):
    if a > b:
        return a
    else:
        return b


# 计算面积
def area(width, height):
    return width * height


# 直接传参
def parameter(str):
    print(str)


# 指定参数名
def parameter1(str, int):
    print(str, int)


# 可变参数
def parameter2(str, *par):
    print(str, par)


# 双星号的参数  会以字典的形式传参
def parameter3(str, **par):
    print(str, par)


# 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：
def parameter4(a, b, *, c):
    return a + b + c


# 匿名函数 lambda
x = lambda a: a + 10

sum = lambda a, b: a + b

# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。

# def method(a,b,/,c,d,*,f):
#     print(a,b,c,d,f)

if __name__ == '__main__':
    hello()
    print(maxNum(3, 4))  #
    area1 = area(4, 5)
    print(area1)
    # 变量是没有具体类型的
    a = "a"
    print(id(a))  # id 查看内存地址变化  1777663212272 内存地址
    a = 1
    print(id(a))  # id 查看内存地址变化  140714303257664 内存地址

    list = [1, 2, 3]
    list1 = ["a", "b"]
    list.append(list1)
    print(list)  # [1, 2, 3, ['a', 'b']]
    # 参数
    parameter("A")  # 直接传参
    parameter(str="S")  # 指定参数名
    parameter1(int=1, str="B")  # 改变参数顺序
    print(1, 23, 4, "ASD")  # 可变参数
    parameter3("YOU", a=1, b="Feng")  # YOU {'a': 1, 'b': 'Feng'}
    print(parameter4(1, 3, c=4))  # 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：
    # 匿名函数
    print(x(31))  # 41
    print(sum(1, 3))  # 4
