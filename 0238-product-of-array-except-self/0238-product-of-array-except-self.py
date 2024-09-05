class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # length = len(nums)
        # result = [1] * length

        # # Calculate left products
        # left_product = 1
        # for i in range(length):
        #     result[i] = left_product
        #     left_product *= nums[i]

        # # Calculate right products and combine with left products
        # right_product = 1
        # for i in range(length - 1, -1, -1):
        #     result[i] *= right_product
        #     right_product *= nums[i]

        # return result


        len_list = len(nums)
        prefix = [1] * len_list
        suffix = [1] * len_list
        for i in range(1, len_list):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len_list-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        return [prefix[i]*suffix[i] for i in range(len_list)]