s=input()

asce=[]
chars=[]
change=[]


for i in range(len(s)):
    asce.append(ord(s[i]))
    #print(asce[i])
    #if asce[i] not in range(65,92) and asce[i] not in range(97,123):
        #asce[i]=83

#print(asce)    

for i in range(0,len(asce)):
    
    if i==0 and asce[i]%2 != 0:
        continue
    if i==len(asce)-1 and asce[i]%2 == 0:
        continue
        
    if asce[i]%2==0:
            
        if asce[i+1] not in range(65,91) and asce[i+1] not in range(97,123):
            asce[i+1]=83
        else:
            if i+1 not in change:
                asce[i+1] += asce[i]%7
        change.append(i+1)
        continue
        
    if asce[i]%2 != 0:
            
        if asce[i-1] not in range(65,91) and asce[i-1] not in range(97,123):
            asce[i-1]=83
        else:
            if i-1 not in change:
                asce[i-1] -= asce[i]%5
        change.append(i-1)
        continue
        
        
    #print(asce)
    #print(change)
        
for i in asce:
    chars.append(chr(i))
    
#print(chars)
    
print("".join(chars))