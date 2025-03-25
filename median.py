x = int(input())
z = []

for i in range(x):
	n  = int(input())
	z.append(n)	

z.sort()

s = x
if s % 2 != 0:
	k = round((s +1)/2) -1
	print(z[k])
elif s % 2 ==0:
	l = round(s/2)-1
	m = round(s/2)
	k= (z[l]+z[m])
	print(k/2)