if __name__ == '__main__':
    namark = []
    mark=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        namark.append([name, score])
        mark.append(score)
    
    mark.sort()
   
    namark.sort()
    
    second_min=mark[1]
    
    for i in namark:
        if (i[1]==second_min):
            print (i[0]) 
         