class Node(object):
	"""docstring for Node"""
	def __init__(self, content = None,hashval = None,previous = None,next = None):
		super(Node, self).__init__()
		self.content = content
		self.hashval = hashval
		self.previous = previous
		self.next = next

class Bucket(object):
	def __init__(self):
		self.sentinel = Node(1,2)
		self.sentinel.next = self.sentinel
		self.sentinel.previous = self.sentinel
		self.m = 4
		self.__count = 0
	def add(self,x = None):
		if x is None:
			pass
		else:
			self.__count+=1
			p = self.sentinel
			#if currently no element in the bucket
			if p.next == self.sentinel:
				self.sentinel.next = Node(x,hash(x),self.sentinel,self.sentinel)
				print(x+' added to bucket, with hash =' +str(hash(x)))
			else:
			# if there is at least one elemetn in the bucket
			#move the p to the rear of the Bucket queue
				while p.next is not self.sentinel:
					p = p.next
			# add a Node accordign to x
				p.next = Node(x,hash(x),p,self.sentinel)
				print(x+' added to bucket, with hash =' +str(hash(x)))
	def checkBucket(self):
		p=self.sentinel
		# print(str(p.content)+' '+str(p.hashval))
		while p.next is not self.sentinel:
			p = p.next
			print(str(p.content)+' '+str(p.hashval))

	def contain(self,x):
		hashOfX = hash(x)
		print('x'+str(x)+' Hash of x:' + str(hash(x)) )
		p = self.sentinel
		if p.next.hashval == hashOfX:
			return True
		#while their is more than the sentinel Node in a bucket
		while p.next is not self.sentinel:
			# print('p move')
			# print(str(p.next.hashval)+'  '+str(hashOfX))
			p = p.next
			if p.hashval == hashOfX:
				return True
			# p = p.next
		return False

	def getcontent(self):
		p = self.sentinel
		while p.next is not self.sentinel:
			p = p.next
			yield (p.content,p.hashval)
		# yield self.content

class HashFramework(object):
	def __init__(self):
		self.__present = [Bucket() for _ in range(4)]
		self.__bucketNumTotal = 4
		self.__n = 0
		self.__m = 4
	def addElementTo_HashFramwork(self,x):
		# choose a Bucket to be added to in a HashFramework
		index_BucketinFram = hash(x) % self.__m		
		print(str(index_BucketinFram))#Check the Fram work
		self.__present[index_BucketinFram].add(x)
		self.__n += 1
		print('HashFramework load----' + str(self.__n/self.__m))

		if self.__n/self.__m >1.5:
			self.reSize()
	
	def printAllBucket(self):
		print('每次运行，字符串都会被放在不同的桶中')
		for buckindex in range(self.__m):
			print('====The content of Bucket # '+str(buckindex) +"====")
			self.__present[buckindex].checkBucket()
	def reSize(self):
		print('resize from '+str(self.__m)+' to '+str(self.__m*2) )

		# self.__bucketNumTotal = self.__bucketNumTotal*2
		self.__m = self.__m*2
		tempPresent = [Bucket() for _ in range(self.__m)]
		for buk in self.__present:
			for contString,hashofString in buk.getcontent():
				print('AAAA '+str(contString) )
				newIndex = hashofString % self.__m
				tempPresent[newIndex].add(contString)
		self.__present = tempPresent



demoFramwork = HashFramework()
demoFramwork.addElementTo_HashFramwork('hello')
demoFramwork.addElementTo_HashFramwork('hello1')
demoFramwork.addElementTo_HashFramwork('hello2')
demoFramwork.addElementTo_HashFramwork('hello3')
demoFramwork.addElementTo_HashFramwork('hello4')
demoFramwork.addElementTo_HashFramwork('hello5')
demoFramwork.addElementTo_HashFramwork('hello6')
demoFramwork.addElementTo_HashFramwork('hello7')
demoFramwork.printAllBucket()
# demoFramwork.addElementTo_HashFramwork('hello1')
# demoFramwork.addElementTo_HashFramwork('hello2')

# demoBucket = Bucket()
# demoBucket.add('hello1')
# demoBucket.add('hello2')
# demoBucket.add('hello3')

# demoBucket.checkBucket()
# print(demoBucket.contain('hello1'))
# print(demoBucket.contain('hello1'))
# print(demoBucket.contain('hello3'))
# print(demoBucket.contain('hello4'))
# print(demoBucket.contain('hello200'))