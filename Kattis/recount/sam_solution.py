# source: https://open.kattis.com/problems/recount

def createList():    # creates list of names voted
    lst = []
    name = str()
    while name != '***':
        name = input()
        lst.append(name)
    return lst[:-1]


def createDict(lst):
    dic = {}
    for name in lst:
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    return dic


def winner():
    dic = createDict(createList())
    chart = sorted(dic.values(), reverse=True)
    if chart[0] == chart[1]:
        return 'Runoff!'
    else:
        for key, value in dic.items():
            if value == chart[0]:
                return key


print(winner())

