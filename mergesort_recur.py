def merge(arr, l, r, m):
	left_len = m - l + 1
	right_len = r - m

    # temp arrays to store sorted halves
	L = arr[l:l+left_len]
	R = arr[m+1:m+1+right_len]

	i, j, k = 0, 0, l;	 

    # both sorted halves are combined in the main array
	while i < left_len and j < right_len:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < left_len:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < right_len:
		arr[k] = R[j]
		j += 1
		k += 1

def mergesort(arr, left, right):
	if left < right:
		mid = left + (right-left)//2
		mergesort(arr, left, mid) 
		mergesort(arr, mid+1, right)
		merge(arr, left, right, mid) # merge the sorted halves


if __name__ == "__main__":
    try:
        arr = [int(x) for x in input("Enter array : ").split()]
        mergesort(arr, 0, len(arr)-1)
        print("Sorted array:", end=" ")
        size = len(arr)
        for i in range(size):
            print(arr[i], end=" ")
        print(end="\n")
        
    except:
        print("Invalid input")
