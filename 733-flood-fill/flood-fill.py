class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        visited = [ [False] * len(image[i]) for i in range(len(image))]
        queue = []
        queue.append((sr, sc))
        while queue:
            i, j = queue.pop()

            if i - 1 >= 0 and not visited[i - 1][j] and image[i - 1][j] == image[i][j]:
                queue.append((i - 1, j))

            if i + 1 <= len(image) - 1 and not visited[i + 1][j] and image[i + 1][j] == image[i][j]:
                queue.append((i + 1, j))

            if  j - 1 >= 0 and not visited[i][j - 1] and image[i][j - 1] == image[i][j]:
                queue.append((i, j - 1))

            if j + 1 <= len(image[i]) - 1 and not visited[i][j + 1] and image[i][j + 1] == image[i][j]:
                queue.append((i, j + 1))

            image[i][j] = color
            visited[i][j] = True

        return image

sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
