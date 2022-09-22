"""
Python3 错误和异常

异常处理
try/except
异常捕捉可以使用 try/except 语句
try:
    执行代码
except:
      发生异常时执行的代码

try 语句按照如下方式工作；

首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。

如果没有异常发生，忽略 except 子句，try 子句执行后结束。

如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。

如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如
except(RuntimeError,TypeError,NameError):

try/except...else
try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。

else 子句将在 try 子句没有发生任何异常的时候执行。

try:
   执行代码
except:
   发生异常时执行的代码
else:
   没有异常时执行的代码


try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码。
try:
   执行代码
except:
   发生异常时执行的代码
else:
   没有异常时执行的代码
finally:
     都会执行

Python 使用 raise 语句抛出一个指定的异常。类似throw


预定义的清理行为
关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
"""
import sys

if __name__ == '__main__':
    try:
        result = 100 / 0
    except ZeroDivisionError:
        print("除数不能为0")

    # 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

    try:
        f = open("D:/myfile.text")
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error:{0}".format(err))  # OS error:[Errno 2] No such file or directory: 'D:/myfile.text'
    except ValueError:
        print("Could not convert data to an integer")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

        # try/except...else

    try:
        f = open("D:/python.text", "r")
    except IOError:
        print('cannot open', f)
    else:
        print('has', f.read(), 'content')  # has 我喜欢下雨天 content
        f.close()

    #  一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
    with open("D:/python.text") as f:  # 不需要手动调用f.close方法
        for line in f:
            print(line, end="")
