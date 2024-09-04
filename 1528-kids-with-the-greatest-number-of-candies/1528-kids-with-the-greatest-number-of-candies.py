class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        bool_res = []

        max_candies = max(candies)

        for i in candies:
            if i + extraCandies >= max_candies:
                bool_res.append(True)
            else:
                bool_res.append(False)

        return bool_res
