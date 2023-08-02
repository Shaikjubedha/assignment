def print_shortest_substring(s,x):
    
    for i in range(0,len(s)-x):
        for j in range(i+x-1,len(s)):
            if s[i]==s[j]:
                ch.append([i,j])
            
 
    
            
    for i in range(len(ch)):
        d=ch[i][1]-ch[i][0]
        
        short.append(d)
    
    

    x=short.index(min(short))
    a=ch[x][0]
    b=ch[x][1]
    
    return s[a:b+1]

s=input()
x=int(input())

ch=[]
short=[]

if x>len(s)-x:
    print("not-found")
    
else:
    y=print_shortest_substring(s,x)



print("x =",x)
print(y)