def total_rabbit_pairs(n, k):
    # Base cases
    if n == 1 or n == 2:
        return 1
    
    # Initialize the first two months
    rabbits = [0] * (n + 1)
    rabbits[1] = 1
    rabbits[2] = 1

    # Compute the number of rabbit pairs for each month upto n
    for i in range(3, n + 1):
        rabbits[i] = rabbits[ i - 1 ] + k * rabbits[ i - 2 ]

    return rabbits[n]

n = 30
k = 4

print(total_rabbit_pairs(n, k))

def rabbit_pairs_fib(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit_pairs_fib(n - 1, k) + k* rabbit_pairs_fib(n - 2, k)
    
print(rabbit_pairs_fib(n,k))