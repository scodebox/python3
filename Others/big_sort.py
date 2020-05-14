def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x),x))


unsorted = ['6','31415926535897932384626433832795','1','3','10','3','5']

op = bigSorting(unsorted)

print (op)
