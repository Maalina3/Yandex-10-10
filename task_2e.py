def main(): 
    N = int(input())

    left, right = [], [0] * (N//2) #так как по условию есть вставки в середину, в какой-то момент может возникнуть ситуация, когда right[0] уже заполнен существующим объектом, придется сдвигать список направо за O(n). Решение - изначально заполнить rigth пустыми элементами
    start_left, stop_left, start_right, stop_right = 0, 0, N//2, N//2
    for _ in range(N):
        action = input().split()
        if action[0] == '+':
            right.append(action[1])
            stop_right += 1
        if action[0] == '-':
            print(left[start_left])
            start_left += 1
        if action[0] == '*':
            if (stop_right - start_right) == (stop_left - start_left):
                left.append(action[1])
                stop_left += 1
            else:
                right[start_right - 1] = action[1]
                start_right -= 1
        if (stop_right - start_right) > (stop_left - start_left):
            left.append(right[start_right])
            stop_left += 1
            start_right += 1
if __name__ == '__main__':
    main()  