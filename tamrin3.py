def sum_all(*args) :
    total = 0
    for i in args :
        total+=i
    return total
print(sum_all(4 , 5, 87, 7 , 9))