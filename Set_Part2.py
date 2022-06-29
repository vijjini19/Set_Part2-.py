'''difference_update'''
# a={12,14,16,18,20}
# b={12,14,6,8,10}
# a.difference_update(b)  #{16,18,20}
# print(a)
# b.difference_update(a)
# print(b)  #{6,8,10}
# a.update(b)
# b.update(a)
# print(a)
# print(b)

'''copy'''
# a={2,4,7}
# a.copy()
# print(a)  #{2,4,7}

'''symmetric_difference_update'''
# a={2,4,6,8,0}
# b={4,6,1,2,9,7}
# a.symmetric_difference_update(b)
# print(a)  #{0,1,7,8,9}
# b.symmetric_difference_update(a)
# print(b)  #{0,1,7,8,9}

'''intersection_update'''
# a={2,4,6,8,0}
# b={4,6,1,2,9,7}
# print(a.intersection(b)) #{2,4,6}
# a.intersection_update(b)
# print(a)
# print(b.intersection(a))  #{2,4,6}

'''remove'''
# a={2,4,6,8,0}
# a.remove(6)
# print(a)  #{0,2,4,8}
# a.remove(34)
# print(a)  #KeyError:34

'''issuperset'''
# a={2,4,6,8,9}
# b={3,5,7,8,0}
# print(a.issuperset(b))  #False
# a={2,4,6}
# b={2,4}
# print(a.issuperset(b))  #True
