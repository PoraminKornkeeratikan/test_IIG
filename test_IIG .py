Arr = [[0,4],[2,3],[2,5],[4,0],[4,2],[4,6],[4,8],[6,2],[6,4],[6,6],[8,1],[8,7]]
for row in range (0,9):
    for col in range (0,9):
        for i in Arr:
            if (row==i[0] and col==i[1]):
                print("*" , end="")
        print(end=" ")
    print (" ")
