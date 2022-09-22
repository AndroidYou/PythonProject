"""
 import 语句
 1.一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行
 2.from ... import语句
 from modename import name1[,name2[,..]]

from ...import*语句

from modename import *   可以一次性的把模块中的所有（函数，变量）名称都导入到当前模块的字符表:

_name_属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，
模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

dir() 函数
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:

包
包是一种管理Python模块命名空间的形式，采用"点模块名称"
 比如  一个模块的名称是A.B ,那么他表示一个包A中的子模块B
使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。

 1. 导入特定模块
 import sound.effects.echo
 使用：sound.effects.echo.echofilter(1234)
 2。 from sound.effects import echo
 使用:echo.echofilter(343)
 3.from sound.effects.echo import echofilter
 使用:echofilter(324)
 4.from sound.effects import *
 Python 会进入文件系统，找到这个包里面所有的子模块，然后一个一个的把它们都导入进来



"""
import sys



def fibo(n):
    a = 0
    b = 1
    while (b < n):
        print(b, end=",")
        a, b = b, a + b


if __name__ == '__main__':
    fibo(100)
    print("当前程序运行")
    # _name_
    # dir(sys)


else:

    print("其他模块运行")
