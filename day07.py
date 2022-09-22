"""
 List 列表
 1.访问 根据下标  [下标]
 2.下标 正序 0 ，1，   倒序 -1，-2
 3.区间访问 [下标1：下标2]  左闭右开区间  下标1 <= X <下标2
 4.更新列表 append
 5.删除元素 del
 6.列表比较 eq  需要导入operation 模块

 列表脚本操作符

 Python 表达式	结果	描述
len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代

列表函数&方法

1	len(list)
列表元素个数
2	max(list)
返回列表元素最大值
3	min(list)
返回列表元素最小值
4	list(seq)
将元组转换为列表



序号	方法
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort( key=None, reverse=False)
对原列表进行排序
10	list.clear()
清空列表
11	list.copy()
复制列表
"""
import operator

if __name__ == '__main__':
    list1 = ["A", "B", "C", "D", "E", "F"]
    print(list1[0])  # A
    print(list1[1])  # B
    print(list1[-2])  # E
    print(list1[1:4])  # ['B', 'C', 'D']
    print(list1[-5:-1])  # ['B', 'C', 'D', 'E']
    print(list1[1:-4])  # ['B']
    # 列表更新
    list1.append("y")
    print(list1)  # ['A', 'B', 'C', 'D', 'E', 'F', 'y']
    # 删除元素
    del list1[-2]
    print(list1)  # ['A', 'B', 'C', 'D', 'E', 'y']
    list__copy = list1.copy()

    print("list1和list__copy是否相等:", operator.eq(list1, list__copy))  # list1和list__copy是否相等: True

    print(list__copy.count("A"))  # 统计A出现的次数 1
    # 反序
    list1.reverse()
    print(list1)  # ['y', 'E', 'D', 'C', 'B', 'A']
    numbers = [1, 2, 3, 4, 5]
    numbers.reverse()
    print(numbers)  # [5, 4, 3, 2, 1]
