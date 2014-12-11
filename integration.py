def romburg(f,a,b,n):
	nums = trapezoid(f,a,b,n)
	newnums = []
	order = 1
	while len(nums)>1:
		for x in range(len(nums)-1):
			newnums.append(((2**(order*2))*nums[x+1]-nums[x])/((2**(order*2))-1))
		nums = newnums
		newnums = []
		order+= 1
		print(nums)
	return nums[0]
			
def trapezoid(f,a,b,n):	
	ans = []
	ans.append(.5*(f(a)+f(b))*(b-a))
	for x in range(1,n+1):
		ans.append(ans[-1]*.5+trap(f,a,b,x))
	print(ans[0])
	print(ans[-1])
	return ans

# Does more than simply trapezoid: this function only
# finds points we can't induct from previous estimations
def trap(f,a,b,n):
	ans = 0 
	_range = b-a
	place = _range/(2**n)
	step = place*2
	while place<_range:
		ans+=f(a+place)
		place+=step
	ans/=2**(n)
	ans*= _range
	return ans

print(romburg(lambda x:x**10,0,2,10))
