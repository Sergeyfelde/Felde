l=7
n=5
m=10
s=0
print('Выберите способ решения: 1 - формулой; 0 - циклом')
a=input()
print('Введите необходимое число')
if a==1:
    k=int(input())
    s=2*k*(l+n+(m*(k+1)/2))
else:
    k=int(input())+1
for i in range(1,k):
    s+=(l + n + i * m)*2
print(s)