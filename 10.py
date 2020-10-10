def contador(string):
    dic = {}
    plvrs = string.split(' ')

    for plvrs in plvrs:
        if plvrs in dic:
            dic[plvrs] += 1
        else:
            dic[plvrs] = 1
    return dic

print(contador("Mariana Alessandra Ana Mariana Ana Ana"))