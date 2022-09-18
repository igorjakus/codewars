def find_missing(sequence):
    a0, an, n = sequence[0], sequence[-1], len(sequence)
    r = (an - a0) // n
    for x in range(a0, an+1, r):
        if x not in sequence:
            return x

def find_missing(sequence):
    for i in range(1, len(sequence)-1):
        if not sequence[i] == (sequence[i+1]+sequence[i-1]) / 2:
            return (sequence[i+1]+sequence[i]) // 2
        
        
find_missing([1, 3, 4, 5, 6, 7, 8, 9])