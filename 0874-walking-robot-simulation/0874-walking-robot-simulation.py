LEFT = -2
RIGHT = -1
class Solution:
    def _turn(self, src: tuple[int, int], cmd: Literal[-1, -2]):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # north, east, south, west
        idx = next(i for i, it in enumerate(directions) if it == src )
        if cmd == LEFT:
            return directions[(idx - 1 + 4) % 4]
        else:
            return directions[(idx + 1) % 4]

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = frozenset(tuple(it) for it in obstacles)

        position = [0, 0]  # (x, y)
        toward = (0, 1)
        answer = 0

        for cmd in commands:
            if cmd in [LEFT, RIGHT]:
                toward = self._turn(toward, cmd)
            else:
                dx, dy = toward
                for _ in range(cmd):
                    x, y = position
                    new_pos = (x + dx, y + dy)
                    if new_pos in obstacles:
                        break
                    position = new_pos
                
                x, y = position
                answer = max(
                    answer,
                    x ** 2 + y ** 2,
                )
        return answer