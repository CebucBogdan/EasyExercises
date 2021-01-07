def quick_sort(sequence):
    lenght = len(sequence)
    if lenght <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    less_than_piv = []
    more_than_piv = []

    for item in sequence:
        if item < pivot:
            less_than_piv.append(item)
        else:
            more_than_piv.append(item)
    return quick_sort(less_than_piv) + [pivot] + quick_sort(more_than_piv)

print(quick_sort([0,3,2,6,9,1]))