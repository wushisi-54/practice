a,b = 1,1
while True:
    print(a)
    a,b = b,a+b
    if a>10000:
        break