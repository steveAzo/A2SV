# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_position = list(zip(position, speed))
        car_position.sort(reverse=True)

        stack = []
        for c in car_position:
            time_to_reach_target = (target - c[0])/c[1]
            if not stack or time_to_reach_target > stack[-1]:
                stack.append(time_to_reach_target)
        
        return len(stack)