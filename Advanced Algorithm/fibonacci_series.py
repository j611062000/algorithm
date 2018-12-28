def fib_series_rec(n):
	"""
	add: hold the value of number of addition
	Once this function is called, we can figure
	out the number of addition for n-th Fibonacci number.
	"""
    global add
    if n <= 2:
        return 1
    else:
    	# If this program enters the stage of "else", the variable, add, 
    	# will increase by one.
        add += 1
        return fib_series_rec(n - 1) + fib_series_rec(n - 2)


for n in range(20):
	add = 0
	fib_series_rec(n)
	print("n: {}, add: {}".format(n,add))

