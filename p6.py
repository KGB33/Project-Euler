#Project Euler Sum Square differnce, Problem 6
#success

def sumsquare():
    i=1
    s=0
    p=0
    ssd=0
    while i < 101:
        s=s+i
        p=p+i*i
        i=i+1
    s=s*s
    ssd=s-p
    print(ssd)

sumsquare()
