class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict = defaultdict(int)
        sum = 0
        count = 0
        dict[0] = 1
        for num in nums:
            sum += num 
            if  ((sum - k) in dict):
                count += dict[sum-k]

            dict[sum] +=1 

        return count