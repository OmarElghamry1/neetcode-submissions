# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quicksort(pairs, 0, len(pairs)-1)
        return pairs

    def _quicksort(self, pairs, s, e): 
        if e - s + 1 <= 1: 
            return 

        left = s
        pivot = pairs[e]

        for i in range(s, e): 
            if pairs[i].key < pivot.key: 
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left +=1
        
        # swap last place with pivot 
        pairs[e] = pairs[left]
        pairs[left] = pivot


        #recursive call 
        self._quicksort(pairs, s, left-1) # before pivot
        self._quicksort(pairs, left+1, e) # after pivot 


    