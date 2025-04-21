def twoSum( nums, target):
    dict = {}

    for i in range(len(nums)):
        dict[nums[i]] = i
        complement = target - nums[i]

        if(complement in dict):
            return [i,dict[complement]]
    
  

print(twoSum([2,3,4,5],5))

       
    