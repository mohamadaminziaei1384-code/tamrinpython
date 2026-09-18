def jostojo(my_list , item) :
    count = 0
    for i in my_list :
        if i == item :
            count+=1
    if count > 0 :
        return True , count
    else:
        return False
my_list = ["gray" , "pink" , "yellow" , "red" , "white" , "green" , "black" ,"yellow", "pink"]
item = input("enter item :")
print(jostojo(my_list , item))