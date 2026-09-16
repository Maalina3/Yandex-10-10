from collections import deque
#изучение методов добавления/удаления в начало/конец за О(1) с помощью deque в готовой библиотеке

def main(): #x
    n, k = (map(int, input().split()))
    stack = list(map(int, input().split()))
    minimum = deque()
    minimum.append(stack[0])
    def clear_minimum(minimum, n):
        if not minimum:
            minimum.append(n)
            return minimum
        if n < minimum[-1]:
            minimum.pop()
            clear_minimum(minimum, n)
        else:
            minimum.append(n)
            return minimum

    for i in range(1, 3):
        clear_minimum(minimum, stack[i])
    print(minimum[0])
    for i in range(3, n):
        if stack[i-3] == minimum[0]:
            minimum.popleft()
        clear_minimum(minimum, stack[i])
        print(minimum[0])

if __name__ == '__main__':
    main()
#