#Getting a prime number between 0 and a number
def isPrime(number):

	a_list = [2]
	for i in range(3,number+1):
		prime = True
		for j in range(2,1):
			if i % j == 0:
				prime == False
		if prime:
			a_list.append(i)
	return(a_list)