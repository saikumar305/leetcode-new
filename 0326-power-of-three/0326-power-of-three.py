class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # def is_power(num):
        #     if num<1: return False
        #     if num == 1: return True
        #     return is_power(num/3)

        # return is_power(n)


        if n < 1:
            return False

        while n%3 == 0:
            n //=3

        return n==1


        