def move_zeros(array):
    zeros = []
    i=0
    while i != array.__len__():
        if (array[i] == 0 or array[i] == 0.0) \
                and type(array[i])!= bool:
            zeros.append(array[i])
            array.pop(i)
            i-=1
        i+=1
    return array + zeros
