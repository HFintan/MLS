def sqrt2():
    c=2; x=0; y=0; r=0; A=0; p=0;
    while (x+1)*(20*p+(x+1))<=2:
        x=x+1
    y=x*(20*p+x)
    r=c-y
    A=x
    for i in range(1,101):
        c=100*r; x=0; y=0; p=A;
        while (x+1)*((20*p)+(x+1))<=c:
            x=x+1
        y=x*(20*p+x)
        r=c-y
        A=A*10+x
        stringA=str(A)
        Ans=stringA[:1] + '.' + stringA[1:]
    print(Ans)
