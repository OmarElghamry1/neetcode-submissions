# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        lol = []
        for i in range(len(pairs)):
            j=i
            while j > 0 and pairs[j].key < pairs[j-1].key: # stable sorting
                pairs[j-1], pairs[j] = pairs[j], pairs[j-1]
                j-=1

            lol.append(pairs[:])
        
        return lol

        
        