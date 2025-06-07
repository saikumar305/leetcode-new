class Solution:
    def findDuplicate(self, array: List[int]) -> int:
        # seen = set()

        # for n in nums:
        #     if n in seen:
        #         return n
        #     seen.add(n)

        # return -1

        # two pointer method

        slow, fast = 0, 0

        while True:

            slow = array[slow]
            fast = array[array[fast]]

            if slow == fast:
                break

        print(slow, fast)

        slow1 = 0

        while True:
            slow = array[slow]
            slow1 = array[slow1]

            if slow == slow1:
                return slow

        