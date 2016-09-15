def bubble_sort(a_list):
	for j in range(len(a_list), 0, -1):
		for i in range(i):
			if a_list[i] > a_list[i+1]:
				a_list[i],a_list[i+1] = a_list[i+1], a_list[i]

def short_bubble_sort(a_list):
    is_exchanges = True
    pass_num = len(a_list)-1
    while pass_num > 0 and is_exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        pass_num -= 1


def insert_sort(a_list):

	for j in range(1,len(a_list)):
		key = a_list[j]

		i = j-1
		while i > 0 and a_list[i] > key:
			a_list[i+1] = a_list[i]
			i -= 1

		a_list[i+1] = key



def merge_sort(a_list):

	if len(a_list) > 1:
		mid = len(a_list) // 2
		left = a_list[:mid]
		right = a_list[mid:]

		return merge(merge_sort(left),merge_sort(right))

	else: return a_list



def merge(left, right):

	i, j = 0, 0
	sorted_list = []

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			key = left[i]
			i += 1
		else:
			key = right[j]
			j += 1
		sorted_list.append(key)

	# while i < len(left):
	# 	sorted_list.append(left[i])
	# 	i += 1
	# while j < len(right):
	# 	sorted_list.append(right[j])
	# 	j += 1
	sorted_list.extend(left[i:])
	sorted_list.extend(right[j:])


	return sorted_list



def quick_sort(a_list):

	def partition(a_list, first, last):
		pivot = a_list[first]

		i = first

		for j in range(i+1, last+1):
			if a_list[j] <= pivot:
				i += 1
				a_list[i], a_list[j] = a_list[j], a_list[i]

		a_list[first], a_list[i] = a_list[i], a_list[first]

		return i

	def quick_sort_helper(a_list, first, last):
		if first < last:
			split_p = partition(a_list, first, last)
			quick_sort_helper(a_list, first, split_p-1)
			quick_sort_helper(a_list, split_p + 1, last)


	quick_sort_helper(a_list, 0 , len(a_list)-1)

	return a_


def min_heap_sort(a_list):


	def build_min_heap(a_list):
		for i in range(len(a_list) // 2 -1, -1, -1):
			min_heapify(a_list, i)
			print a_list

	def min_heapify(a_list, i):
		l = 2 * i + 1
		r = 2 * i + 2
		smallest = i

		if l < len(a_list) and a_list[i] > a_list[l]:
			smallest = l
		if r < len(a_list) and a_list[smallest] > a_list[r]:
			smallest = r

		print smallest, i
		if smallest != i:
			a_list[i], a_list[smallest] = a_list[smallest], a_list[i]
			min_heapify(a_list, smallest)
		print a_list


	build_min_heap(a_list)
	ascend_list = []
	for i in range(len(a_list)-1, -1, -1):
		a_list[i], a_list[0] = a_list[0], a_list[i]
		ascend_list.append(a_list.pop())
		min_heapify(a_list, 0)

	return ascend_list































