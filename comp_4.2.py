import sys

def main():
    input_data = sys.stdin.read().splitlines()
    idx = 0

    n = int(input_data[idx]); idx += 1

    queue = []
    for _ in range(n):
        line = input_data[idx]; idx += 1
        name, length = line.rsplit(maxsplit=1)
        queue.append((name, int(length)))
    queue.reverse()

    m = int(input_data[idx]); idx += 1
    events = []
    for _ in range(m):
        parts = input_data[idx].split(); idx += 1
        events.append((int(parts[0]), parts[1], int(parts[2])))

    current_time = 0
    ei = 0

    while ei < m and events[ei][0] == 0:
        _, nname, nlength = events[ei]
        ei += 1
        queue.append((nname, nlength))

    while queue or ei < m:
        if not queue:
            t = events[ei][0]
            current_time = max(current_time, t)
            while ei < m and events[ei][0] == t:
                _, nname, nlength = events[ei]
                ei += 1
                queue.append((nname, nlength))
            continue

        name, length = queue.pop()
        end_time = current_time + length

        while ei < m and events[ei][0] < end_time:
            _, nname, nlength = events[ei]
            ei += 1
            queue.append((nname, nlength))

        print(name, current_time)
        current_time = end_time

        while ei < m and events[ei][0] == current_time:
            _, nname, nlength = events[ei]
            ei += 1
            queue.append((nname, nlength))

if __name__ == '__main__':
    main()
