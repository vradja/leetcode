class Solution:
    def valid_str_index(self, string, index):
        backspaces = 0
        while index >= 0:
            if string[index] == "#":
                backspaces += 1
            elif backspaces > 0:
                backspaces -= 1
            else:
                break

            index -= 1

        return index

    def backspaceCompare(self, S: str, T: str) -> bool:
        left_str_index, right_str_index = len(S) - 1, len(T) - 1

        while left_str_index >= 0 or right_str_index >= 0:
            left_str_index = self.valid_str_index(S, left_str_index)
            right_str_index = self.valid_str_index(T, right_str_index)

            if left_str_index < 0 and right_str_index < 0:
                return True
            elif left_str_index < 0 or right_str_index < 0:
                return False
            elif S[left_str_index] != T[right_str_index]:
                return False

            left_str_index -= 1
            right_str_index -= 1

        return True

    # Pop and Append Solution
    def backspaceCompare_2(self, S: str, T: str) -> bool:
        S_new, T_new = list(), list()

        for i in S:
            if i == "#":
                if S_new:
                    S_new.pop()  # nothing to backspace if the first char itself is #
            else:
                S_new.append(i)

        for j in T:
            if j == "#":
                if T_new:
                    T_new.pop()
            else:
                T_new.append(j)

        return S_new == T_new


sol = Solution()

# print(sol.backspaceCompare("xy#z", "xzz#"))
# print(sol.backspaceCompare("xy#z", "xyz#"))
# print(sol.backspaceCompare("xp#", "xyz##"))
# print(sol.backspaceCompare("xywrrmp", "xywrrmu#p"))
# print(sol.backspaceCompare("bbbextm", "bbb#extm"))
# print(sol.backspaceCompare("nzp#o#g", "b#nzp#o#g"))
print(sol.backspaceCompare("aaa###a", "aaaa###a"))
