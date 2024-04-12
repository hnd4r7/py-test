from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        

        def check(p1, p2, p3):
            def div(x,y):
                if y == 0:
                    return 0
                else: return x/y
            return div((p1[1]-p2[1]) , (p1[0]-p2[0])) == div((p2[1]-p3[1]) , (p2[0]-p3[0]))
        
        for i in range(len(coordinates)-3):
           if not check(coordinates[i],coordinates[i+1],coordinates[i+2]):
                return False
        return True
        
Solution().checkStraightLine([[1,2],[2,3],[3,5]])