from colorama import Fore, Back, Style
# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]
# 		print(Back.GREEN + str(L))

		# into 2 halves
		R = arr[mid:]
# 		print(Back.RED + str(R))

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
            
		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
		print(Back.CYAN + str(L))
		print(Back.BLUE + str(R))
# Code to print the list


def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':
	arr = [34, 25, 20, 5, 44, 12,9]
	print("Tartibsiz array:", end="\n")
	printList(arr)
	mergeSort(arr)
	print(Style.RESET_ALL + "Tartibli array: ", end="\n")
	printList(arr)

# This code is contributed by Mayank Khanna
