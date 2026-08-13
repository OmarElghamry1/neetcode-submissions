class Solution:
    def binary_search(self, arr, target): 

        l, r = 0, len(arr)-1
    
        while l <= r: 
            mid = (l+r)//2
        
            if target > arr[mid]: 
                l = mid + 1
            elif target < arr[mid]: 
                r = mid -1
            else: 
                return True
                
        return False
    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L, R = 0, len(matrix)-1

        while L <= R: 
            mid = (L + R)//2

            if target > matrix[mid][-1]: 
                L = mid + 1

            elif target < matrix[mid][0]: 
                R = mid -1

            else: 
                return self.binary_search(matrix[mid], target)

        return False

            



    














    
