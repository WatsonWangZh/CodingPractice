# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # # M1.偷懒法，调库排序返回第k个元素即可
        # nums.sort(reverse=True)
        # return nums[k-1]

        # M2.分治法，思想类似快排 时间复杂度O(n)
        def partition(nums, l, r):
            pivot = nums[r]
            i = l-1
            for j in range(l, r):
                if nums[j] >= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[r] = nums[r], nums[r+1]
            return i+1

        l , r = 0, len(nums)-1
        while True:
            pivot_index = partition(nums, l ,r)
            if pivot_index == k-1:
                return nums[pivot_index]
            elif pivot_index < k-1:
                l = pivot_index + 1
            else:
                r = pivot_index - 1 

        # # M3.第k大/k小问题，直觉用堆，维护容量为k的最大堆，时间复杂度O(nlogk)
        # import heapq
        # heapq.heapify(nums)
        # return heapq.nlargest(k,nums)[-1]

        # # M4.PriorityQueue
        # import queue
        # q = queue.PriorityQueue()
        # for i in nums: q.put(-i)
        # for i in range(1, len(nums)+1):
        #     temp = q.get()
        #     if i == k: return -temp