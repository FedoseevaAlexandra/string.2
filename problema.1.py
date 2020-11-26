cuv=str(input('introdu cuv :'))
k=str(input('introdu o litera :'))
if len(k)==1:
    for i in cuv:
        x=cuv.replace(i,k)
        print(x)