a = [i for i in range(1,101)]
#print(a)
for b,c in enumerate (a):
	if c%15==0:
		a[b] = 'fizzbuzz'
	elif c%5==0:
		a[b] = 'buzz'
	elif c%3==0:
		a[b] = 'fizz'
print(a)
