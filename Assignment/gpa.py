def main():
	n = int(input("Subject number:"))
	while n<0 or n>5:
		n = int(input("Subject number:"))
	subject_list = []
	for i in range(n):
		grade = int(input(f"Grade{i}:"))
		subject_list.append(grade)
	print(subject_list)
	avg = float(sum(subject_list)/n)
	print(avg)

if __name__ == "__main__":
	main()