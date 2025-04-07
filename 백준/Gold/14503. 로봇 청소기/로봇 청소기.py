import sys
input = sys.stdin.readline
def parse_input():

    N, M = map(int, input().split())
    r, c, d = map(int, input().split())

    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    return N, M, r, c, d, grid


def robot_vacuum(N, M, r, c, d, grid):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    cleaned_count = 0
    cleaned_positions = set()

    def can_move(x, y):
        return 0 <= x < N and 0 <= y < M and grid[x][y] == 0

    while True:
        if (r, c) not in cleaned_positions:
            cleaned_positions.add((r, c))
            cleaned_count += 1

        cleaned = False
        for i in range(4):
            d = (d + 3) % 4
            nr, nc = r + moves[d][0], c + moves[d][1]

            if can_move(nr, nc) and (nr, nc) not in cleaned_positions:
                r, c = nr, nc
                cleaned = True
                break

        if not cleaned:
            # Move backward
            nr, nc = r - moves[d][0], c - moves[d][1]
            if not can_move(nr, nc):
                break
            r, c = nr, nc

    return cleaned_count


def main():
    N, M, r, c, d, grid = parse_input()
    result = robot_vacuum(N, M, r, c, d, grid)
    print(result)


if __name__ == "__main__":
    main()
