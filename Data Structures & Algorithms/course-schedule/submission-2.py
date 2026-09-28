class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        path = set()
        seen = set()

        def dfs(course):
            if course in seen:
                return True
            if course in path:
                return False

            path.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            path.remove(course)
            seen.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True