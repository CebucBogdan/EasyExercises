def bubble(sequence):
    length = len(sequence)-1
    sorting = False
    while not sorting:
        sorting = True
        for i in range(0,length):
            if sequence[i] > sequence[i+1]:
                sequence[i],sequence[i+1] = sequence[i+1],sequence[i]
                sorting = False

    return sequence
print(bubble([1,7,5,3,2,4]))