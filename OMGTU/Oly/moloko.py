f=open("input1.txt")
N = int(f.readline())
d = []
for i in range(N):
    s=f.readline().split(" ")
    X1 = int(s[0])
    Y1 = int(s[1])
    Z1 = int(s[2])
    C1 = float(s[6])
    X2 = int(s[3])
    Y2 = int(s[4])
    Z2 = int(s[5])
    C2 = float(s[7])
    d.append(round((C2-((C1*(X2*Y2+Y2*Z2+X2*Z2))/(X1*Y1+Y1*Z1+X1*Z1)))/(((X2*Y2*Z2)/(1000))-((X1*Y1*Z1*(X2*Y2+Y2*Z2+X2*Z2))/(1000*(X1*Y1+Y1*Z1+X1*Z1)))),2))
print(f"{d.index(min(d))+1} {min(d)}")

