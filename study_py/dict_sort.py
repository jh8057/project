dict = {'Marry':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}

aa = sorted(dict)
print(aa)
bb = sorted(dict.items())
print(bb)
cc = sorted(dict.items(),key= lambda x : x[1])
print(cc) 
dd = sorted(dict.items(),key= lambda x : x[1] , reverse=True)
print(dd) 