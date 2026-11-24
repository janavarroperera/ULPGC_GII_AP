def part(list, low, high):
    i = low
    pivote = list[high]
    for j in range(low, high):
        if list[j] > pivote:
            list[j], list[i] = list[i], list[j]
            i += 1
    list[i], list[high] = list[high], list[i]
    return i

def quicksort(list, low, high):
    if low < high:
        p = part(list, low, high)
        quicksort(list, low, p-1)
        quicksort(list, p+1, high)
        return
    return

list = [1, 3, 5, 9, 7]
quicksort(list, 0, len(list) - 1)
print(list)