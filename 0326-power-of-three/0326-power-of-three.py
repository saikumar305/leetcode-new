class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def is_power(num):
            if num<1: return False
            if num == 1: return True
            return is_power(num/3)

        return is_power(n)


        