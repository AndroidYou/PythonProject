"""
 Set 集合
  集合是一个无序的不重复元素序列
  可以使用大括号{ } 或set{ } 函数创建集合
  1.创建空集合  只能使用 set()
  2.添加元素
           add() 单个元素,
           update()单个或多个，参数可以是列表，元组，字典等

  3.移除元素  remove() ,discard()
  4.随机删除 pop()
  5.计算元素个数 len
  6.清空集合 clear
  7.判断元素在集合中是否存在  x in s


add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素

"""