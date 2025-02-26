sys.set_int_max_str_digits(10**4)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        hashMap={"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        def stoi(num):
            ans=0
            for i in num:
                ans=ans*10 + hashMap[i]
            return ans
        return str(stoi(num1) + stoi(num2))
        