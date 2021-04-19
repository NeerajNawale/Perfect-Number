#No. is perfect or Not
def perfect(n):
	sum = 1
	for i in range(2, (n//2)+1):
		if n%i == 0:
			sum += i
		# print(i)
	return sum

n = int(input("Enter a number --> "))
if n == 1:
    print("NO")
elif (perfect(n) == n):
    print("YES")
else:
    print("NO")
