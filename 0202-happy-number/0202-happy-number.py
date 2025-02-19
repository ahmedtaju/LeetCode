class Solution:
    def squareSum(x):
        sum = 0
        while x:
            digit=x%10
            sum += digit * digit
            x//=10
        return sum
    def isHappy(self, n: int) -> bool:
        def squareSum(x):
            sum = 0
            while x:
                digit=x%10
                sum += digit * digit
                x//=10
            return sum
        hashSet = set()
        while n!=1:
            n=squareSum(n)
            if n in hashSet:
                return False
            else:
                hashSet.add(n)
        return True


        