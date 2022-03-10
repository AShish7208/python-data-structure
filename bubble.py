def bubble_sort(nums):


    nums = list(nums)  

    
    for _ in range(len(nums)-1):
    
        for i in range(len(nums)-1):

            if nums[i] > nums[i+1]:

                nums[i],nums[i+1] = nums[i+1],nums[i]


        return nums

nums = [5,1,16,1,6,41,5,4,4,151]
result  = bubble_sort(nums)
print(result)
