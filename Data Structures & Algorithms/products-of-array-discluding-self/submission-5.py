class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        prefix.append(nums[0])
        for i in range(1,len(nums)):
            product = prefix[i-1] * nums[i]
            prefix.append(product)
        
        postfix.append(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            product = postfix[-1] * nums[i]
            postfix.append(product)
        postfix.reverse()
        output = []
        for i in range(0,len(nums)):
            if (i == 0):
                output.append(1*postfix[i+1])
            elif (i == len(nums)-1):
                output.append(prefix[i-1]*1 )
            else:
                output.append(prefix[i-1]*postfix[i+1] )


        return output
