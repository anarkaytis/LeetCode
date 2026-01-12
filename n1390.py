class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
        total = 0
        for num in nums:
            for prime in primes:
                if prime * prime > num:
                    break
                elif num % prime == 0:
                    second = num // prime
                    if prime * prime == num:
                        break
                    elif prime * prime * prime == num:
                        total += 1 + num + second + prime
                    else:
                        for prime_2 in primes:
                            if prime_2 * prime_2 > second:
                                total += 1 + num + second + prime 
                                break 
                            elif second % prime_2 == 0:
                                break
                    break
        
        return total
