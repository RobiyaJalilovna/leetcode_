class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i=1
        while(1):
            if((n*i)%2==0):
                return n*i
                break
            else:
                i=i+1