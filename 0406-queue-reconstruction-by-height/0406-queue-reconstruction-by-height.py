class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        ans = []
        for i in people:
            ans.insert(i[1],i)
        return ans