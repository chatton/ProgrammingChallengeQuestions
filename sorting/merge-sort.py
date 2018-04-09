
def merge_sort(arr):
    if arr:
        mid = (int)(len(arr) / 2)

        left_half = arr[:mid]
        right_half = arr[mid + 1:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(arr)


arr = [11, 2, 5, 4, 7, 56, 2, 12, 23]
merge_sort(arr)
