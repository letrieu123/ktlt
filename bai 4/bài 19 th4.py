print("sinh vien:le thanh khanh trieu MSV:235752021610117")
def sieve_of_eratosthenes(limit):
    #nguyên tố
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 và 1 không phải số nguyên tố
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, limit + 1, start):
                sieve[i] = False  # Đánh dấu các số không phải là số nguyên tố
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return tuple(primes)
P = sieve_of_eratosthenes(1000000)
print(f"Tuple P có {len(P)} số nguyên tố nhỏ hơn 1 triệu.")
print(f"Những số nguyên tố đầu tiên trong tuple P là: {P[:10]}")  # In ra 10 số nguyên tố đầu tiên
