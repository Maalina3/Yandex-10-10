# def main():
#     n, k = int(input()), int(input())
#     stack = list(map(int, input().split()))
#     minimum = []
#     start, stop = 0, 0
#     for i in range(0, n-k+1):
#         if stop - start == 0:
#             minimum.append(stack[i])
#             stop += 1
#         if i != 0:
#             if stack[i-1] == minimum[start]:
#                 start += 1
#         if stack[i+1] <= minimum[stop]



# if __name__ == '__main__':
#     main()
# #