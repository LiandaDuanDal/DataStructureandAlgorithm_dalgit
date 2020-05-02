# import datetime
# starttime = datetime.datetime.now()
# #long running
# #do something other
# endtime = datetime.datetime.now()
# print (endtime - starttime).second


#选择排序
# small -> huge
class SelectiveSorter(object):
	def __init__(self, initialList):
		self.__listToSort = initialList
	def sortSelf(self):
		lenOfList = len(self.__listToSort)
		for i in range(lenOfList-1):
			for j in  range(i+1,lenOfList):
				if self.__listToSort[j]<self.__listToSort[i]:
					temp_i = self.__listToSort[i] 
					self.__listToSort[i] = self.__listToSort[j]
					self.__listToSort[j] = temp_i 
	def printCurrentList(self):
		print(self.__listToSort)

demoList = [1,7,2,6,3,5,4]
demoSorter = SelectiveSorter(demoList)
demoSorter.printCurrentList()
demoSorter.sortSelf()
demoSorter.printCurrentList()


print('pull request test')
