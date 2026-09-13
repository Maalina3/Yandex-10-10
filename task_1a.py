import sys


def main():
    
    n = input()
    stack = []

    for i in n:
        if i == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        elif i == ']' and len(stack) > 0 and stack[-1] == '[':
            stack.pop()
        elif i == '}' and len(stack) > 0 and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(i)
            break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()
