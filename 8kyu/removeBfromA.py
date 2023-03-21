# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b keeping their order.
#
# array_diff([1, 2], [1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1, 2, 2, 2, 3], [2]) == [1, 3]

#################### My Solution ####################

# a lista não necessariamente vai estar ordenada, por isso eh preciso checar todos
# os valores
def array_diff(a, b):
    # o array a é percorrido de trás pra frente, para que quando
    # algum valor seja removido, isso não mude a posição dos próximos elementos a serem percorridos
    for i in reversed(range(len(a))):
        if a[i] in b:  # se o elemento está contido em B ele é removido de A
            del a[i]
    return a
