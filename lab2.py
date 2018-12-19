a = [5, 10, 15, 20, 25]
def new_list(a):
	b = [a[0], a[-1]]
	return b


c = new_list(a)
print (c)
fibonachi = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in fibonachi:
	if num < 5:
		print(num)
common_list = []
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in fibonachi:
	if i in d:
		common_list.append(i)

