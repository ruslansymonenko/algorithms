def find_smallest(array):
    if not array:
        return -1

    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest_index

def selection_sort(array):
    for i in range(len(array)):
        smallest_index = find_smallest(array[i:]) + i

        array[i], array[smallest_index] = array[smallest_index], array[i]

    return array

print(selection_sort([4, 3, 2, 1]))