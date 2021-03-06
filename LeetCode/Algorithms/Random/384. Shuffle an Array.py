# Shuffle a set of numbers without duplicates.

# Example:
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# // Shuffle the array [1,2,3] and return its result. 
# Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.init = list(nums)
        self.curr = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.init
        
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.curr)
        for i in range(n):
            j = random.randint(i,n-1)
            self.curr[i], self.curr[j] = self.curr[j], self.curr[i]
        return self.curr

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()