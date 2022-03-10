def insertion_sort(nums):
    for i in range(1,len(nums)):
        curr = nums[i]
        j = i-1
        while j>=0 and nums[j]>curr:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = curr
    return nums
