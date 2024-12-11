## Asymptotic Analysis  
Time Complexity: `O(n)`  
Space Complexity: `O(1)`  


&nbsp;  


## Personal Stats
| Date Solved | Time Taken |
| ----------- | ---------- |
| 12-11-2024 | 3min |  
| 11-08-2024 | 3min |  
| 11-06-2024 | 2.5min |  
| 10-30-2024 | 4min |  
| 10-17-2024 | 2hr+ |  


&nbsp;  


## Notes  

<details>
    <summary>Solved the first time in 15min but hit TLE (Time Limit Exceeded)</summary>
    
        class Solution(object):
        def rotate(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: None Do not return anything, modify nums in-place instead.
            """
            k = k % len(nums)

            subt = len(nums) - k

            if k == 0:
                return None
            
            for i in range(subt):
                nums.append(nums[i])

            for j in range(subt):
                nums.pop(0)        
</details>

<details>
    <summary>Another TLE case (due to time complexity)</summary>
    
        class Solution(object):
            def rotate(self, nums, k):
                """
                :type nums: List[int]
                :type k: int
                :rtype: None Do not return anything, modify nums in-place instead.
                """
                k = k % len(nums)

                if k == 0:
                    return None

                loop = len(nums) - k

                for index in range(loop, len(nums)):
                    i = index
                    for j in range(loop):
                        temp = nums[i]
                        nums[i] = nums[i-1]
                        nums[i-1] = temp

                        i -= 1

</details>
