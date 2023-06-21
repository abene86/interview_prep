nums = [5, 6, 9, 11, 1, 2, 3]

def mergesort(nums:list[int])->list[int]:
    if len(nums) == 1:
        return nums
    mid_index = len(nums) // 2
    list_1 =  nums[:mid_index]
    list_2 =  nums[mid_index:]
    res_1 = mergesort(list_1)
    res_2 = mergesort(list_2)
    return combine_res(res_1, res_2)

def combine_res(res_1:list[int], res_2:list[int])->list[int]:
    index_1= 0
    index_2= 0
    ans =[]
    while index_1 < len(res_1) and index_2 < len(res_2):
        if res_1[index_1] < res_2[index_2]:
            ans.append(res_1[index_1])
            index_1 +=1
        elif res_2[index_2] < res_1[index_1]:
            ans.append(res_2[index_2])
            index_2 +=1
        else:
            ans.append(res_2[index_2])
            index_2+=1
            indedx_1+=1
    if index_1 < len(res_1):
        ans = ans + res_1[index_1 :]
    if index_2 < len(res_2):
        ans = ans + res_2[index_2 :]
    return ans

            
            
print(mergesort(nums))



