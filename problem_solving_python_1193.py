X=int(input()) #3

line=1
while X>line: #3>1
    X-=line #X=2
    line+=1 #line=2
    
if line%2==0:
    a=X #a=2
    b=line-X+1 #b=1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')