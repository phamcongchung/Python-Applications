#generate 2 halves of a pyramid with height input
#each half has a bottom length equal to the height
#each half is 2 spaces apart from the other
def main():
	n = int(input("Insert pyramid height:"))
	while n>8 or n<=0:
		n = int(input("Insert again:"))
	for i in range(n):
		print(" "*(n-i-1)+"#"*(i+1)+"  "+"#"*(i+1))

if __name__ == '__main__':
	main()