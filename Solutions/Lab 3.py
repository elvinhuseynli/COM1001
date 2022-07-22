inputs=input().split()
inputs_2=input().split()
m=0
p=0
z=[]
for x in inputs:
    for y in inputs_2:
        m=0
        p=0
        z=[]
        while p<len(x):
            if y in x[p:len(y)+p]:
                m+=1
                z.append(p)
                p+=len(y)
            else:
                p+=1
        if m!=0:
            l=x+' '+y+' '+str(m)+' '+str(z)
            print(l)

