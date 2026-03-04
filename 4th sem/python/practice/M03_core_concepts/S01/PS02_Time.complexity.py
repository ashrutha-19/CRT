nums = [1,2,3,4]
res = []
s = 0
for ele in nums:
    s = s + ele
    res.append(s)
print(res)

ans = []
for i in range(1,len(nums)+1):
    ans.append(sum(nums[:i]))
print(ans)

#code id 1672
nums =[[1, 2, 3][3, 2, 1]]
res =[]
s = 0
for ele in nums:
    s = s + ele
    res.append(s)
print((max)res)
