class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_list = []
        larger_list = []
        pivot_list = []

        for n in nums:
            if n < pivot:
                smaller_list.append(n)
            elif n > pivot:
                larger_list.append(n)
            else:
                pivot_list.append(n)
        
        return smaller_list + pivot_list + larger_list