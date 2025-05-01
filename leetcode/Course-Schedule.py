from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
