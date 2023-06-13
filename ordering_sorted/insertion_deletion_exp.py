import random

class SpecialArray:
    def __init__(self):
        self.num=[num+1 for num in range(50)]

    def insert(self, target:int)->None:
        target_index = self.helper_find_index(target)
        first_half = self.num[0:target_index]
        second_half = self.num[target_index:]
        first_half.append(target)
        self.num = first_half + second_half

    def helper_find_index(self, target:int)->int:
        start_index =0
        while start_index < len(self.num):
            if target < self.num[start_index]:
                break
            start_index+=1
        return start_index

    def delete(self, target:int)->bool:
        if len(self.num) == 0:
            return false
        target_index = self.binarySearch(target)
        #target_index = self.helper_binary_rec(self.num, target)
        if target_index == -1:
            return False
        first_half = self.num[:target_index]
        second_half=self.num[target_index+1:]
        self.num = first_half + second_half
        return True

    def binarySearch(self, target:int)->int:
        arr_copy = self.num.copy()
        while len(arr_copy) != 0:
            mid_index = len(arr_copy) // 2
            if arr_copy[mid_index] == target:
                break
            if target > arr_copy[mid_index]:
                arr_copy = arr_copy[mid_index+1:]
            else:
                arr_copy = arr_copy[:mid_index]
            if len(arr_copy) == 0:
                mid_index =-1
                break
        return mid_index
    def helper_binary_rec(self, arr:list, target:int)->int:
        if len(arr) == 0:
            return -1
        mid_index = len(arr) // 2
        if target == arr[mid_index]:
            return mid_index
        if target > arr[mid_index]:
            return self.helper_binary_rec(arr[mid_index+1:],target)
        else: 
            return self.helper_binary_rec(arr[:mid_index],target)
            
        
    def __str__(self)->str:
        str_arr = [str(ele) for ele in self.num]
        return " ".join(str_arr)        

def random_numb_gen()->int:
    return random.randint(1, 50)

super_array = SpecialArray()
print(super_array)
for index in range(10000):
    random_num = random_numb_gen()
    super_array.insert(random_num)
    random_num = random_numb_gen()
    super_array.delete(random_num)
    print(super_array)





