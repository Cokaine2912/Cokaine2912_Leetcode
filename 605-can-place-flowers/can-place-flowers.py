class Solution:
    def canPlaceFlowers(self, bed: List[int], n: int) -> bool:

        prev = 0 
        
        plant = 0
        for i in range(len(bed)) :
            if i == len(bed) - 1 :
                if prev == 0 and bed[i] == 0 :
                    plant += 1
                    bed[i] = 1 
                     
                break

            next = bed[i + 1]
            if prev == 0 and next == 0 and bed[i] == 0 :
                plant += 1 
                bed[i] = 1
                 
            prev = bed[i]
            # next = bed[i + 1]

        
        return True if plant >= n else False
             

        