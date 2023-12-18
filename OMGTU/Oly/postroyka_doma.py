# Ремонт 1
# Ремонт 2
# Ремонт 3
# Ремонт 4
# Старый материал 5
# Старый материал 6
# Полностью новые стены 7
# Ремонт 8
# Ремонт 9
# Ремонт 10
# Ремонт 11
# Старый материал 12
# Полностью новые стены 13
# Ремонт 14
f = open(f"input_s1_14.txt").readline()
s = f.split(" ")
X = int(s[0])
Y = int(s[1])
L = int(s[2])
C1 = int(s[3])
C2 = int(s[4])
C3 = int(s[5])
C4 = int(s[6])
C5 = int(s[7])
C6 = int(s[8])
if min(C2 + C6 + C4 + C5, C2 + C3, C1) == C2 + C6 + C4 + C5:  # Полностью новые стены
    sum = L * (C2 + C6) + 2 * (X + Y) * (C4 + C5)
elif min(C2 + C6 + C4 + C5, C2 + C3, C1) == C2 + C3:  # Старый материал
    if L <= 2 * (X + Y):
        sum = L * (C2 + C3) + (2 * (X + Y) - L) * (C4 + C5)
    else:
        sum = 2 * (X + Y) * (C2 + C3) + (L - (2 * (X + Y))) * (C2 + C6)
else:  # Ремонт
    if L <= 2 * (X + Y):
        if L > max(X, Y):
            if C2 + C3 < C2 + C6 + C4 + C5:
                sum = (L - max(X, Y)) * (C2 + C3) + (2 * (X + Y) - L) * (C4 + C5) + max(X, Y) * C1
            else:
                sum = (L - max(X, Y)) * (C2 + C6 + C4 + C5) + (2 * (X + Y) - L) * (C4 + C5) + max(X, Y) * C1
        else:
            sum = (2 * (X + Y) - L) * (C4 + C5) + L * C1
    else:
        if C2 + C3 < C2 + C6 + C4 + C5:
            sum = (L - max(X, Y)) * (C2) + (2 * (X + Y) - max(X, Y)) * (C3) + max(X, Y) * C1 + (L - 2 * (X + Y)) * C6
        else:
            sum = (L - max(X, Y)) * (C2 + C6) + max(X, Y) * C1 + (2 * (X + Y) - max(X, Y)) * (C4 + C5)
print(sum)
