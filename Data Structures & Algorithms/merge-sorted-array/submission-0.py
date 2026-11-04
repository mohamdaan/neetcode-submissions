class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
      #  i = 0 #nums1 pointer
      #  j = 0 # nums2 pointer
      #  if nums1[i] > nums2[j]:
      #      temp = nums1[i]
       #     nums1[i] = nums2[j]
       #     nums2[j] = temp
       #     i +=1  
        #else:

        #go through nums2 and insert each index into m then m+1 etc
        for num in nums2:
            nums1[m] = num
            m+=1
        print(nums1)
        nums1.sort()

        