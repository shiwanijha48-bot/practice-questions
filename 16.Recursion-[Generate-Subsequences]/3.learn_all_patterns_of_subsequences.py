class Solution:
    def solve(self, index, s, curr, st):
        if index == len(s):
            st.add("".join(curr))
            return

        # Don't take current character
        self.solve(index + 1, s, curr, st)

        # Take current character
        curr.append(s[index])
        self.solve(index + 1, s, curr, st)
        curr.pop()          # Backtracking

    def countDistinct(self, s):
        st = set()
        self.solve(0, s, [], st)
        st.remove("")       # Remove empty subsequence
        return len(st)

    def betterString(self, s1, s2):
        cnt1 = self.countDistinct(s1)
        cnt2 = self.countDistinct(s2)

        if cnt1 >= cnt2:
            return s1
        return s2
    

    #  TLE 
    #  THATS WHY LATER ON WE WILL USE DP TOO HAVE OPTIMAL SOLUTION
    