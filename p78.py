import sys,time

def main():
	n=1
	partition = [1]
	signs = [1,1,-1,-1]
	while(True):
		partition.append(0)
		i = 0
		penta = 1
		while( n-penta >= 0):
			sign = signs[i%4]
			partition[n] += sign * partition[n-penta]
			partition[n] = partition[n] % 1000000
			i +=1
			if i % 2 == 0:
				j = i/2 + 1
			else:
				j = -1*(i/2 + 1)
			penta = j*(3*j -1)/2

		if partition[n]==0:
			print n
			return n
		n +=1

if __name__ =="__main__":
	s = time.time()
	main()
	print "Total time taken:", time.time()-s,"seconds"
