def solution(wallpaper):
    minx, miny, maxx, maxy = 51, 51, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                minx = min(minx, i)
                miny = min(miny, j)
                maxx = max(maxx, i+1)
                maxy = max(maxy, j+1)
    
    return [minx, miny, maxx, maxy]

# 간단한 브루트포스 문제