# class ProorityQueue(object):
#  	"""docstring for ProorityQueue"""
#  	def __init__(self:
#  		super(ProorityQueue, self).__init__()
#  		self.arg = arg

class NodeObj(object):
	def __init__(self,left = 0,content = 0,right = 0):
		self.left = left
		self.content = content
		self.right = right
		# self.childrenCount = 0
		self.printNode()
	def printNode(self):
		print('left-',str(self.left),'--content-',str(self.content),'--right-',str(self.right))

class Min_Heap(object):
 	"""docstring for ClassName"""
 	def __init__(self):
 		self.Tree = NodeObj()
 	def addNode(self,content):
 		#initial position: the Botton of the tree
 		#first search for the bottom
 		pass
 	def swimUp(self):
 		pass

# implimentation of comparing algorithm
# object:
# Determine if their is any duplicates in the array

# A silly method
def sillySearch(x):
	OperationCount = 0
	# print('I compare every possible pair!')
	lengthOfX = len(x)
	for _ in range(lengthOfX):
		currentA = x[_]
		for i in range(_+1,lengthOfX):
			OperationCount +=1
			# print("Comparing ",str(x[_])+"=="+str(x[i]),"Operation Count: ",str(OperationCount))
			if x[_]==x[i]:
				# print(str(x[_])+"="+str(x[i]))
				return True

# a little bit cleverer method
# only consider the neighboring duplication
def betterSearch(x):
	OperationCount = 0
	# print('I compare neighboring pairs!')
	lengthOfX = len(x)
	for _ in range(lengthOfX-1):
		currentA = x[_]
		OperationCount +=1
		# print("Comparing ",str(x[_])+"=="+str(x[_+1]),"Operation Count: ",str(OperationCount))
		if x[_]==x[_+1]:
			# print(str(x[_])+"="+str(x[_+1]))
			return True

# demoMH = Min_Heap()
# x = 0.333333333333
# print(x.as_integer_ratio())
# import datetime
# from matplotlib import pyplot as plt
# x = [-3,-1,2,4,4,8,12]

# sillyRecorder = []
# betterRecorder = []
# #test silly
# for N in range(1,1000,100):
# 	start = datetime.datetime.now()
# 	x = list(range(0,N-1))
# 	x.append(N-2)
# 	sillySearch(x)
# 	    # do something
# 	end = datetime.datetime.now()
# 	# print((end-start).microseconds)
# 	sillyRecorder.append((end-start).microseconds)
# 	# sillyRecorder.append()
# for N in range(1,1000,100):
# 	x = list(range(0,N-1))
# 	x.append(N-2)
# 	start = datetime.datetime.now()
# 	betterSearch(x)
# 	    # do something
# 	end = datetime.datetime.now()
# 	# print((end-start).microseconds)
# 	betterRecorder.append((end-start).microseconds)
# 	# sillyRecorder.append()

# plt.plot(sillyRecorder)
# plt.plot(betterRecorder)
# plt.legend(['silly','better'])
# plt.show()
# print(sillyRecorder)
 

 # access Operation Counting:
def sillySearch_Count(x):
	OperationCount = 0
	# print('I compare every possible pair!')
	lengthOfX = len(x)
	for _ in range(lengthOfX):
		currentA = x[_]
		for i in range(_+1,lengthOfX):
			OperationCount +=1
			# print("Comparing ",str(x[_])+"=="+str(x[i]),"Operation Count: ",str(OperationCount))
			if x[_]==x[i]:
				# print(str(x[_])+"="+str(x[i]))
				return True


def betterSearch_Count(x):
	OperationCount = 0
	# print('I compare neighboring pairs!')
	lengthOfX = len(x)
	for _ in range(lengthOfX-1):
		currentA = x[_]
		OperationCount +=1
		# print("Comparing ",str(x[_])+"=="+str(x[_+1]),"Operation Count: ",str(OperationCount))
		if x[_]==x[_+1]:
			# print(str(x[_])+"="+str(x[_+1]))
			return True




print((.1+.1+.1)==.3)

print(360 + 360 +360== 360.0+360.0+360.0)

print(360/7)
print(360.0/7)


