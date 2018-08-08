# coding: utf-8

if __name__ == "__main__":
    # 字典定义
    m1 = {"Alice": "2341", "Beth": "9102", "Ceil": "3158"}
    items = [("name", "Taylor"), ("age", 42)]
    m2 = dict(items)
    print m1, m2
    # 基本操作
    people = {
        "Alice": {
            "phone": "2341",
            "addr": "Foo drive 23"
        },
        "Beth": {
            "phone": "9102",
            "addr": "Bar street 42"
        },
        "Ceil": {
            "phone": "3158",
            "addr": "Baz avenue 90"
        },
    }
    lables = {
        "phone": "phone number",
        "addr": "address"
    }
    name = raw_input("Name: ")  # 输入名字
    request = raw_input("Phone number (p) or address (a)? ")
    if request == "p": key = "phone"
    if request == "a": key = "addr"
    if name in people:
        print "%s's %s is %s." % (name, lables[key], people[name][key])
    # 字典格式化字符串
    m3 = {"Alice": "2341", "Beth": "9102", "Ceil": "3158"}
    print "Ceil's phone number is %(Ceil)s" % m3
    # HTML格式化操作
    template = '''
    <html>
    <head><title>%(title)s</title></head>
    <body>
    <h1>%(title)s</h1>
    <p>%(text)s</p>
    </body>
    '''
    data = {"title": "My Home page", "text": "Welcome to my home page!"}
    print template % data
