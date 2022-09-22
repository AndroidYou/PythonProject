"""
  List 列表
  1. 列表中的元素类型可以不相同
  2. 列表是写在方括号[] 之间，用逗号分隔开的元素列表
  3.列表可以被索引和截取  列表被截取后返回一个包含所需元素的新列表
  语法格式：
   变量 [头下标 ：尾下标]  左闭右开

     追加元素： append
   
   索引值以0为开始值，-1为从末尾的开始位置
   
   array = [ A , B , C , D , E ,F ] 
   索引正序   0   1   2   3   4  5
       倒序  -6  -5  -4  -3  -2 -1

   4.List 有序集合 列表截取   [-1:-1]  元素可以修改 list = [1,2,3]
   5.Tuple 有序 元组  元素不能修改   trup = (1,2,3)
   6.Set 无集合 是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员
       功能：进行成员关系测试和删除重复元素
       构建： 使用{} 或set()    创建空集合只能使用 set（）
   7。Dictionary 字典 无需的对象集合 类似于map  通过键key存取
      字典是一种映射类型，字典用{ } 标识   它是一个无序的 键(KEY):值(VALUE)  键必须使用不可变类型
      在同一个字典中，键KEY必须是唯一的 不能重复

"""
array = ["A", "B", "C", "D", "E", "F"]
lis = [1, 2]


def reverseWords(input):
    inputWords = input.split(" ")
    """
      第一个参数 -1 表示最后一个元素
      第二个参数  空 表示移动到列表末尾
      第三个参数  -1 变色逆向
    """
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output


if __name__ == '__main__':
    print("Hello Study List")
    print(array[1])  # B
    print(array[-1])  # F
    print(array[1:])  # ['B', 'C', 'D', 'E', 'F']
    print(array + lis)  # ['A', 'B', 'C', 'D', 'E', 'F', 1, 2]
    print(lis * 2)  # [1, 2, 1, 2]
    print(array[2:4])  # ['C', 'D']  左闭右开 相当于   2=<x <4
    array[2] = 10
    print(array)  # ['A', 'B', 10, 'D', 'E', 'F'] 可以修改元素值
    rw = reverseWords('I heat you')  # you heat I 逆向输出
    print(rw)

    """
     元组
    """
    tuple = (123, "YOU", 58, 134, "HELLO")
    tinytuple = ("123", 322)
    print(tuple)  # (123, 'YOU', 58, 134, 'HELLO')
    print(tuple[0])  # 123
    print(tuple[1:3])  # ('YOU', 58)
    print(tuple + tinytuple)  # (123, 'YOU', 58, 134, 'HELLO', '123', 322)

    tup1 = ()
    tup2 = (1,)
    print(tup1)  # ()
    print(tup2)  # (1,)
    """
      set 集合
    """
    aSet = {1, 2, 3, "12", 3, "12"}
    print(aSet)  # {1, 2, 3, '12'}  去重复
    # 成员判断
    if "123" in aSet:
        print("数据已存在")
    else:
        print("不存在")  # 不存在

    """
       集合运算
    """
    bSet = set("ABC")
    cSet = set("avc")

    print(bSet - cSet)  # bSet 和 cSet差集 # {'B', 'A', 'C'}
    print(bSet | cSet)  # 并集 {'B', 'a', 'A', 'C', 'v', 'c'}
    print(bSet & cSet)  # 交集  set() 空
    print(bSet ^ cSet)  # 不同时存在的元素 {'v', 'B', 'c', 'A', 'a', 'C'}

    """
     Dictionary 字典
    """
    dict = {}
    dict["you"] = 3
    dict['android'] = 10
    print(dict)  # {'you': 3, 'android': 10}
    print(dict.values())  # dict_values([3, 10])
    print(dict.keys())  # dict_keys(['you', 'android'])
