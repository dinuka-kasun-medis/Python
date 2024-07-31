def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("This method only works for odd-order magic squares.")
    
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2
    
    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        newi, newj = (i - 1) % n, (j + 1) % n
        if magic_square[newi][newj]:
            i += 1
        else:
            i, j = newi, newj

    return magic_square

def print_magic_square(magic_square):
    for row in magic_square:
        print(" ".join(str(num).rjust(3) for num in row))

#Example usage:
n = int(input("Add odd-order magic square number : "))
magic_square = generate_magic_square(n)
print_magic_square(magic_square)

