





def deg(num):
	a = list(num)
	a.insert(0, '0')
	for i in range(len(a)):
		index = len(a) - i - 1
		z = int(a[index])*2
		a[index] = str(z)
	for i in range(len(a)):
		index = len(a) - i - 1
		if len(a[index])>1:
			a[index-1] = str(int(a[index-1]) + int(a[index][:1]))
			a[index] = a[index][-1:]
	
	return a
		


answer = '1'

for i in range(1000):
	answer = deg(answer)

answer = answer[701::]

print(''.join(answer))








