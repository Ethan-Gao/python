# coding: utf-8

if __name__ == "__main__":
    # 非字典方式
    names = ["Alice", "Beth", "Ceil", "Dee", "Ella"]
    numbers = ["2341", "9102", "3158", "0142","5551"]
    print names.index("Dee"), numbers[names.index("Dee")]
    # 字典方式
    phonebook = {"Alice": "2341", "Beth": "9102", "Ceil": "3158", "Dee": "0142", "Ella": "5551"}
    print phonebook["Beth"]
