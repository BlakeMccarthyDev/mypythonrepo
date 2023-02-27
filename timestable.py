
tt = 7

for i in range(4):
    print("--------------\n" + str(tt) + " Times Table \n--------------")
    for i in range(13):
        val = tt * i
        if(val != 0):
            print(val)
        else: 
            pass
    tt += 1
