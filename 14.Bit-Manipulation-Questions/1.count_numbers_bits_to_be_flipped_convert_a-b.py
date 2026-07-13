def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        count = 0
        for i in range(0, 32):
            if res & (1<<i) != 0:
                count += 1
        return count
        # tc = o(32), sc = o(1)