# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self._mergesort(pairs, 0, len(pairs) - 1)
        return pairs

    def _mergesort(self, arr, start, end):
        if end - start +1 <= 1:
            return 

        m = (start + end) // 2

        self._mergesort(arr, start, m)
        self._mergesort(arr, m+1, end)

        self._sort(arr, start, m, end)

    def _sort(self, arr, start, m, end): 

        l_arr = arr[start:m+1] # [start: end-1]
        r_arr = arr[m+1:end+1]
        
        l = r = 0
        k = start # start
        while l < len(l_arr)  and r < len(r_arr): 
            if l_arr[l].key <= r_arr[r].key: 
                arr[k] = l_arr[l]
                l+=1

            else:
                arr[k] = r_arr[r]
                r+=1
            
            k+=1

        #left_overs
        while l < len(l_arr): 
            arr[k] = l_arr[l]
            l+=1
            k+=1

        
        while r < len(r_arr): 
            arr[k] = r_arr[r]
            r+=1
            k+=1


        return 



        




            