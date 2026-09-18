class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        curr_max = 0
        for p, s in cars:
            t = (target - p) / s

            if t > curr_max:
                fleets += 1
                curr_max = t

        return fleets
        
        