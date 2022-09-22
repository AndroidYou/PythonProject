"""
 数据结构

 一，列表
  1.列表可以修改，而字符串和元组不能
  2.列表方法
list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	移除列表中的所有项，等于del a[:]。
list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	返回 x 在列表中出现的次数。
list.sort()	对列表中的元素进行排序。
list.reverse()	倒排列表中的元素。
list.copy()	返回列表的浅复制，等于a[:]。

  3.将列表当做堆栈使用
  列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）.
  用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
  4.将列表当做队列使用
  可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
  在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
  5.列表推导式
  6.元组和序列
  元组由若干逗号分隔的值组成，输出时总是有括号的，以便于正确表达嵌套结构，

"""

from collections import deque

if __name__ == '__main__':
    # 将列表当做队列使用
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.append("Graham")

    print(queue.popleft())  # Eric
    print(queue.popleft())  # John

    # 列表推导式
    vec = [x for x in range(10)]
    print(vec)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    str = [' banana', ' loganberry', ' apple']
    print([item.strip() for item in str])  # ['banana', 'loganberry', 'apple'] 去除空格

    list1 = [[x, x * 2] for x in vec]
    print(list1)  # [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18]]

    del list1[:]
    print(list1)  # [] 删除集合

    # 元组
    t = 1232, 435, 456, "sadfs"
    print(t)  # (1232, 435, 456, 'sadfs')
    print(t[1])  # 435
    # 集合
    
