#给定一个整数数组 num 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
def twosum(nums:list,target:int):
  for a in range(len(nums)):
    for b in range(len(nums)):
      if nums[a]+nums[b]==target and a!=b :
        return nums.index(a),nums.index(b)
print(twosum([1, 2, 4], 6) ,  end='')
