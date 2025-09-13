import matplotlib
print(matplotlib.__version__)


nums = [1,2,3]
for i in nums:
    nums.append(i)
    print(len(nums))
    if len(nums) > 6:
        break

print(nums)