# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        n, m = len(img), len(img[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                total = 0
                count = 0
                dir_x = [i-1, i, i+1]
                dir_y = [j-1, j, j+1]

                for x in dir_x:
                    for y in dir_y:
                        if 0 <= x <= n-1 and 0 <=y <= m-1:
                            total += img[x][y]
                            count += 1
                res[i][j] = total//count
        
        return res
                