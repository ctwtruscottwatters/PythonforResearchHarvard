def is_prime(n):
	steps = 0
	for x in range(2, n, 1):
		steps += 1
		for y in range(2, x, 1):
			steps += 1
			if x % y == 0:
				steps += 3
				break
			else:
				print("{} is prime".format(x))
				steps += 2
				break
		steps += 1
		print("Steps: ", steps)
def main():
	is_prime(100000)
	
if __name__ == "__main__": main()