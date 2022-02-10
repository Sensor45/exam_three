
def func(list):

    dic = {}

    for i in list:

        if isinstance(i, float):
            dic.update({'float': i})

        elif isinstance(i, str):
            dic.update({'str': i})

        elif isinstance(i, bool):
            dic.update({'bool': i})

        elif isinstance(i, int):
            dic.update({'int': i})

        else:
            dic.update({'none': i})

    return dic

list = [1, 4.7, 'hi', False, None]

print(func(list))
