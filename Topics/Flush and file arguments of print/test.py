# # start = input("Enter the knight's starting position:").split()
# # print(len(start))
# # print(start[0].isdigit() and start[1].isdigit())
# #
# # M = []
# # for i in range(8):
# #     M.append([])
# #     # print(M)
# #     for j in range(8):
# #         M[i].append('-')
# M = [['-' for j in range(8)] for i in range(8)]
# n = 0
# row = 8
# border_line = '-' * 19
# x = list(range(9))
# print(border_line)
# while n < (len(M) - 1):
#     for line in M:
#         print(row, '| ', *M[n], ' |')
#         n += 1
#         row -= 1
#
# print(border_line)
# print(*x)
lis = input().split()
x, y = lis.sp
print(x)
print(y)
