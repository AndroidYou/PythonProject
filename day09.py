"""
 字典 Dictionary 相当于map
 1.以键值对的方式存储数据 key:Value  使用花括号 { }
 2.key必须是唯一的，value可以重复
 3.创建空字典  { }或使用函数 dict()
 4.字典访问：dict["KEY"]
 5.修改value  dict["key"] = newValue
 6.删除字典元素 del dict['key']
 7.清空字典 del dict


内置函数

1	len(dict)
计算字典元素个数，即键的总数。

3
2	str(dict)
输出字典，可以打印的字符串表示。

"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
3	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。

1   dict.clear() 删除字典内所有元素
2	dict.copy()  返回一个字典的浅复制
3	dict.fromkeys() 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	dict.get(key, default=None) 返回指定键的值，如果键不在字典中返回 default 设置的默认值
5	key in dict 如果键在字典dict里返回true，否则返回false
6	dict.items() 以列表返回一个视图对象
7	dict.keys()  返回一个视图对象
8	dict.setdefault(key, default=None)  和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	dict.update(dict2)  把字典dict2的键/值对更新到dict里
10	dict.values()  返回一个视图对象
11	pop(key[,default])  删除字典 key（键）所对应的值，返回被删除的值。
12	popitem()  返回并删除字典中的最后一对键和值。

"""

if __name__ == '__main__':
    tinyDict = {"A": 10, "b": 9, "f": 31, "l": 0}
