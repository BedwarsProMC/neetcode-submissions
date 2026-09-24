class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for i in range(numCourses)]

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        path = set()
        done = set()

        def dfs(course):
            if course in path: #cycel so IMPOSSIOBLE
                return False

            if course in done: # this node been fully explored already so optimisation
                return True

            path.add(course)

            for pre in adjList[course]:
                if not dfs(pre):
                    return False

            path.remove(course) # backtrack.
            done.add(course) # thiscourse fully explored and has no cycles

            return True


        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
        