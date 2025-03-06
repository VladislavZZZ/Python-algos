class Solution:

    def get_cell_count(self, c_prev, n):
        return c_prev + 4 * (n - 1)

    def coloredCells_o_n(self, n: int) -> int:
        c_prev = 1
        for it in range(0, n):
            c_prev = self.get_cell_count(c_prev, it + 1)

        return c_prev

    def coloredCells_o_1(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)


if __name__ == '__main__':
    sol = Solution()
    n = 10000
    sol.coloredCells_o_n(n)
    sol.coloredCells_o_1(n)