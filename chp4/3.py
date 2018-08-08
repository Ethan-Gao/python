# coding: utf-8

if __name__ == "__main__":
    # clear
    x = {}
    y = x
    x["key"] = "value"
    print x, y
    x.clear()
    print x, y
    # copy
    x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
    y = x.copy()
    y['username'] = 'mlh'
    print x, y
    y['machines'].remove('bar')
    y['machines'].append("new")
    print x, y
    # fromkeys
    print {}.fromkeys(["name", "age"]), dict.fromkeys(["name", "age"]), \
        dict.fromkeys(["name", "age"], "(unknown)")
    # get
    x = {"alina": "29", "lily": "32"}
    print x.get("alina"), x.get("anna"), x.get("crystal", "N/A")
