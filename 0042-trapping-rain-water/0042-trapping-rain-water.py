class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        width = len(height)

        @cache
        def get_right_wall(pivot: int):
            if pivot == width - 1:
                return height[pivot]
            return max(height[pivot + 1], get_right_wall(pivot + 1))

        @cache
        def get_left_wall(pivot: int):
            if pivot == 0:
                return height[pivot]
            return max(height[pivot - 1], get_left_wall(pivot - 1))

        answer = 0
        for i in range(width):
            me = height[i]

            min_wall = min(get_left_wall(i), get_right_wall(i))
            answer += max(min_wall - me, 0)

        return answer
