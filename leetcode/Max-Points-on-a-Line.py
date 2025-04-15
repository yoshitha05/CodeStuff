from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:
                return (float('inf'), 0)
            g = gcd(dy, dx)
            return (dy // g, dx // g)

        if len(points) <= 2:
            return len(points)

        max_points = 0

        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicate = 1
            local_max = 0

            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    duplicate += 1
                else:
                    s = slope(points[i], points[j])
                    slopes[s] += 1
                    local_max = max(local_max, slopes[s])

            max_points = max(max_points, local_max + duplicate)

        return max_points
