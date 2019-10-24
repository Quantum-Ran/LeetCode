class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list1 = []

        def recursion(level_left, level_right, level_max, S):
            if len(S) == 2 * level_max:
                list1.append(S)
                return
            if level_left < level_max:
                recursion(level_left + 1, level_right, level_max, S + '(')
            if level_right < level_left:
                recursion(level_left, level_right + 1, level_max, S + ')')

        recursion(0, 0, n, '')
        return list1
