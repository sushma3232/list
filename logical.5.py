def fun(a):
    i=0
    g=[]
    while i<len(a):
        b=str(a[i])
        n=""
        j=0
        while j<len(b):
            if b[j]!="0":
                n=n+b[j]
            j=j+1
        v=int(n)
        g.append(v)
        i=i+1
    print(g)
fun([1200,1502,14020,200])
            
                