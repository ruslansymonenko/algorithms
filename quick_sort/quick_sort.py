def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        base = arr[0]

        less = [i for i in arr[1:] if i <= base]
        greater = [i for i in arr[1:] if i > base]

        return quick_sort(less) + [base] + quick_sort(greater)

print(quick_sort([5, 4, 3, 2, 1]))