# Multiplying integer numbers of n, m bit length (base 10) - Find x * y = ?
# Karatsuba algorithm is to divide the numbers in H (high bits) and L (low bits)
# Example: 123456 is 123 - H and 456 - L
# Then:
# a = x(high) * y(high)
# d = x(low) * y(low)
# e = (x(high) + x(low))(y(high) +y(low)) - a - d
# result is x * y = a.10^n + e.10^n/2 + d

# n, m is length of numbers respectively, 10 is because base 10

def karatsuba(x, y):
    # figure out n:
    n = max(len(str(x)), len(str(y)))
    mid = n // 2
    # no need to implement the algorithm for small numbers
    if x < 10 or y < 10:
        return x * y
    # split the numbers
    x_high, x_low = divmod(x, 10**mid)
    y_high, y_low = divmod(y, 10**mid)
    # recursively call the split again, so we can multiply small numbers later on
    d = karatsuba(x_low, y_low)
    e = karatsuba(x_high + x_low, y_high + y_low)
    a = karatsuba(x_high, y_high)

    return (a * (10 ** n)) + ((e - d - a) * (10 ** mid)) + d


if __name__ == "__main__":
    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967627

    result = karatsuba(num1, num2)
    result2 = num1 * num2
    delta = result - result2
    print(f"The result is: {result}")
    print(f"No Karatsuba: {result2}")
    print(f"Difference: {delta}")
