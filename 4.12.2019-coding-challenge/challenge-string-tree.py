def christmas_tree_(leaf, num_of_layers):
    if num_of_layers <=0:
        return None
    leafer = -1
    for i in range(num_of_layers, 0, -1):
        leafer +=2
        print(((i-1)*' ')+(leafer*leaf))

def christmas_tree(string,num):
    if num <=0:
        return None
    leafer = -1
    out = ''
    for i in range(num, 0, -1):
        leafer +=2
        if i == 1:
            out += ((i-1)*' ')+(leafer*string)
        else:
            out += ((i-1)*' ')+(leafer*string)+'\n'
    return out

christmas_tree_('#',-5)

