def karatsuba_multiply(x, y):
    # Base case
    if x < 10 or y < 10:
        return x * y
    
    # Splitting
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2
    
    a, b = divmod(x, 10**n2)
    c, d = divmod(y, 10**n2)
    
    # Recursive calls
    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    ad_bc = karatsuba_multiply(a + b, c + d) - ac - bd
    
    # Combine results
    result = ac * 10**(2*n2) + ad_bc * 10**n2 + bd
    
    return result

# Example usage
x = 123456789
y = 987654321
product = karatsuba_multiply(x, y)
print(product)
