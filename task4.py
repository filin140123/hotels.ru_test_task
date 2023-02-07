# Скорость O(n)
def is_prime(n: int) -> bool:
    for i in range(2, n):
        if not n % i:
            return False
    return True


# Скорость O(√n)
def is_prime_optimized(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True
