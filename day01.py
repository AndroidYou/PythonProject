"""
基本语法
"""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 1.我是单行注释

# 2.定义变量不需要指定类型，直接定义即可
word = "字符串"

# 3.等号(=)是用来赋值
counter = 20  # 整数变量
miles = 1000.1  # 浮点型类型
name = "HELLO"  # 字符串类型
# 4.多个变量赋值
a = b = c = 1

e, f, g = 1, 2, "3"

# 5.六种数据类型
# 一,Number 数字 二,String 字符串 三,List 列表 四,Tuple 元组 五,Set集合 六,Dictionary 字典
# 不可变数据 Number String Tuple 可变数据 List Dictionary Set

# 6.python3中 bool是int的子类 True和False可以和数字相加 True==1,False == 0，返回True
# 注：一个变量可以通过赋值指向不同的对象

# 7.字符串：索引值以0位开始，-1为从末尾的开始位置
str = "youfeng"
# 8. 反斜杠 \ 转义特殊字符，如果不想转义在字符串前面添加 r


if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi(word)
    # input("\n按下 enter键后退出当前输入\n") 命令行输入
    print(counter, miles, name)
    print(type(a))  # <class 'int'>  type()函数用来查询对象类型，子类不是父类类型
    print(isinstance(a, int))  # True  isinstance 用来判断对象类型，子类是父类类型
    print(issubclass(bool, int))  # True
    print(str[0])  # y
    print(str)  # youfeng
    print(str[0:])  # 从0 遍历输出  youfeng
    print(str[0:-1])  # 从0遍历输出到倒数第二位 youfen
    print(str * 2)  # youfengyoufeng 连续输出2遍
    print('you\nfeng')
    # 输出
    ''' 
    you
    feng
    '''
    print(r"you\nfeng")  # you\feng 禁止转义

# Python中的字符串是不能改变的
