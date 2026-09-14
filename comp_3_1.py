import sys

def main():
    n, m = map(int, input().split())
    grid = [input() for i in range(n)]

    for row in grid:
        blocks = []
        count = 0
        for ch in row:
            if ch == '#':
                count += 1
            else:
                if count > 0:
                    blocks.append(count)
                    count = 0
        if count > 0:
            blocks.append(count)
        print(len(blocks), *blocks)
    print()
    for j in range(m):
        blocks = []
        count = 0
        for i in range(n):
            if grid[i][j] == '#':
                count += 1
            else:
                if count > 0:
                    blocks.append(count)
                    count = 0
        if count > 0:
            blocks.append(count)
        print(len(blocks), *blocks)


if __name__ == '__main__':
    main()