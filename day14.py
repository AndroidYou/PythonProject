"""
 迭代器

 迭代器 有两个基本方法：inter()   创建迭代器对象  和next() 输出迭代器的下一个元素
 字符串，列表或元组对象都可用于创建迭代器

把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。


StopIteration
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

生成器 在Python中 使用了yield的函数被称为生成器
 生成器是一个返回迭代器的函数，只能用于迭代操作，返回一个迭代器的对象
"""
import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


if __name__ == '__main__':
    list = [1, 2, 3, 4]
    iterator = iter(list)
    print(next(iterator))  # 1
    for x in iterator:
        print(x, end="")  # 1,2 3, 4

    print()
    generator = fibonacci(10)
    while True:
        try:
            print(next(generator), end=",")
        except StopIteration:
            sys.exit()
