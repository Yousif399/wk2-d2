# exercise1-a
def less_than_ten(number):
    n = [x for x in number if x < 10]
    n.sort()
    return n
print(less_than_ten([17,3,12,32,1,10,12,88,6]))
#b
def number(n):
    result = []
    for x in n:
        if x < 10:
            result.append(x)
    return result
print(number([17,30,12,32,1,10,12,88,6]))

# Exercise 2
l_1 = [15,9,1,2,3,4,5,6]
l_2 = [11,3,4,5,6,7,8,10]

def mr_li(l_1,l_2):
    new_list=l_1+l_2
    new_list.sort()
    return new_list
print(mr_li(l_1,l_2))

