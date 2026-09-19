from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses
        # 0 = unvisited
        # 1 = visiting
        # 2 = visited

        def dfs(course):

            if state[course] == 1:
                return False      # Cycle found

            if state[course] == 2:
                return True       # Already checked

            state[course] = 1

            for nxt in graph[course]:

                if not dfs(nxt):
                    return False

            state[course] = 2

            return True

        for i in range(numCourses):

            if not dfs(i):
                return False

        return True