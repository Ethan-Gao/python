# coding: utf-8

if __name__ == "__main__":
    # list函数
    print list("hello"), list(str(12345)), list("q1@e:s9")

    # 列表基本操作
    ### 赋值/修改元素
    x = [None] * 10
    print x
    x[0], x[1], x[5] = 0, 10, 5
    print x
    x[0] = None
    print x
    ### 删除元素
    y = [1, 2, 3, 4, 5]
    del y[0]
    print y, y[0], len(y)

    # 分片赋值
    x, y, z = list("hello"), [1, 5], list("perl")
    x[1:3] = [1, 2, 3]
    y[1:1] = [2, 3, 4, 'h']
    z[1:] = list("ython")
    print x, y, z
    x[1:] = []
    y[2:] = list("add")
    z[-2:] = [3, 4, 5]
    print x, y, z

    # 列表方法
    ### append
    x, y, z = [1, 2, 3], ["to", "be", "or", "not", "to", "be"], [[1, 2], 1, 1, [2, 1, [1, 2]], [1, 2], 1]
    x.append(4)
    print x, y.count("to"), z.count([1, 2]), z.count(1)
    x.extend(y)
    print x
    ### extend
    a1, a2 = [1, 2], [3, 4]
    print a1, a2, a1 + a2
    a1.extend(a2)
    print a1, a2
    ### 链接字符串
    a1, a2 = [1, 2], [3, 4]
    b1, b2 = [1, 2], [3, 4]
    a1 = a1 + a2
    b1[len(b1):] = b2
    print a1, a2, b1, b2
    ### index
    c1 = ["today", "is", "a", "good", "day"]
    print c1.index("is")
    ### insert
    x = [1, 2, 3, 4, 5]
    x.insert(3, "insert")
    print x
    x[4:4] = ["four"]
    print x
    ### pop
    x = [1, 2, 3, 4]
    print x.pop(), x
    x.append(x.pop())
    print x
    ### remove
    x = ["to", "be", "or", "not", "to", "be"]
    x.remove("to")
    print x
    ### reverse
    x = [1, 2, 3, 4]
    x.reverse()
    print x
    ### sort
    x = [4, 6, 2, 1, 7, 9]
    y = x.sort()
    print x, y
    ### 排序副本
    ### 方法1:先将x复制一份当作y，然后使用sort对y进行排序
    x = [4, 6, 2, 1, 7, 9]
    y = x[:]
    y.sort()
    print x, y
    ### 方法2:使用sorted函数
    x = [4, 6, 2, 1, 7, 9]
    y = sorted(x)
    print x, y
    ### compare
    ### 不理解 ###
