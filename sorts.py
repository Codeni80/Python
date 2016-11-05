

def selectionSort(list):
	for fill in range(len(list) - 1, 0, -1):
		maxPos = 0
		for loc in range(1, fill + 1):
			if list[loc] > list[maxPos]:
				maxPos = loc
		tmp = list[fill]
		list[fill] = list[maxPos]
		list[maxPos] = tmp
		
def bubbleSort(list):
	for j in range(len(list) - 1, 0, -1):
		for i in range(j):
			if list[i] > list[i+1]:
				tmp = list[i]
				list[i] = list[i + 1]
				list[i + 1] = tmp
				
def insertionSort(list):
	for i in range(1, len(list)):
		curr = list[i]
		pos = i
		
		while pos > 0 and list[pos - 1] > curr:
			list[pos] = list[pos - 1]
			pos = pos - 1
		list[pos] = curr
		
def mergeSort(list):
	if len(list) > 1:
		mid = len(list)//2
		left = list[:mid]
		right = list[mid:]
		
		mergeSort(left)
		mergeSort(right)
		i = 0
		j = 0
		k = 0
		
		while i < len(left) and j < len(right):
			if left[i] < right[i]:
				list[k] = left[i]
				i = i + 1
			else: 
				list[k] = right[j]
				j = j + 1
			k = k + 1

		while i < len(left): 
			list[k] = left[i]
			i = i + 1
			k = k + 1
		
		while j < len(right):
			list[k] = right[j]
			j = j + 1
			k = k + 1
	
def quickSort(list):
	qsHelper(list, 0, len(list) - 1)
	
def qsHelper(list, first, last):
	if first < last:
		split = part(list, first, last)
	
		qsHelper(list, first, split - 1)
		qsHelper(list, split + 1, last)
	
def part(list, first, last):
	pivot = list[first]
	
	left = first + 1
	right = last
	done = False
	
	while not done:
		while left <= right and list[left] <= pivot:
			left = left + 1
		while list[right] >= pivot and right >= left:
			right = right - 1
			
		if right < left:
			done = True
		else:
			tmp = list[left]
			list[left] = list[right]
			list[right] = tmp
			
	tmp = list[first]
	list[first] = list[right]
	list[right] = tmp
	
	return right
		
