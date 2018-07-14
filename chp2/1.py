# coding: utf-8

if __name__ == "__main__":
    # 普通序列
    tom = ['Tom Curise', 76]
    john = ['John Smith', 50]
    lary = ['Lary Page', 53]
    will = ['Will Smith', 58]
    print tom, john, lary, will
    # 包含序列的序列
    database1 = [tom, john]
    database2 = [lary, will]
    print database1, database2
    # 多重序列
    database = [database1, database2]
    print database
