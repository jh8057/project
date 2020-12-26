fruit = ["사과", "사과","사과","사과", "바나나","바나나" , "키위","키위", "딸기","딸기","딸기"]

d = {}



for i in fruit:
    if i in d:
        d[i] = d[i] +1
    else:
        d[i] = 1
        
print(d)
    

    

