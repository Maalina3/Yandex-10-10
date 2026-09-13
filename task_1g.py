n = 10
number = list(map(int, input().split())) 

stack = []
stack_index = []
res = [-1] * n

for i in range(n):
    if len(stack) == 0:
        stack.append(number[i])
        stack_index.append(i)
        continue
    while number[i] < stack[-1]:
        res[stack_index[-1]] = i
        stack.pop()
        stack_index.pop()
        if len(stack) == 0:
            break
    
    stack.append(number[i])
    stack_index.append(i)
print(*res)
