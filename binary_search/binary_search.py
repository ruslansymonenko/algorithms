def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        guess = array[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(binary_search(my_array, 10))
print(binary_search(my_array, 100))