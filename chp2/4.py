# coding: utf-8

if __name__ == "__main__":
    ### 2.4.0
    # 元组可以省略()
    x = 1, 2, 3
    print x
    # 空元组使用()表示
    x, y = (1, 2, 3), ()
    print x, y
    # 一个元素的元组
    x = 4,
    y = (5,)
    print x, y
    # 实例
    x = 3 * (40 + 2)
    y = 3 * (40 + 2,)
    print x, y

    ### 2.4.1
    # 参数为序列
    x = [1, 2, 3]
    y = tuple(x)
    print y, tuple(["he", "llo"])
    # 参数为元组
    x = (123, )
    print tuple(x), tuple([1, 2, "hello"])

    ### 2.4.2
    x = (1, 2, 3)
    print x[:2], x[-2:]
