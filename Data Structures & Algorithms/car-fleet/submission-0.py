class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        time_map = {}

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            time_map[position[i]] = time

        for pos in sorted(time_map.keys(), reverse=True):

    
            if not stack or time_map[pos] > stack[-1]:
                stack.append(time_map[pos])

        return len(stack)