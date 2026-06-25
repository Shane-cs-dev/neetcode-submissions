class Solution:
    def scoreOfString(self, s: str) -> int:
        stack = []
        ans = 0
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                prev_ch = stack.pop()
                ans += abs(ord(ch) - ord(prev_ch))
                stack.append(ch)
        
        return ans