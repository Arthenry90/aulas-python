input_start = int(input("Digite o número de inicio "))
input_end = int(input("Digite o número de fim "))

# if input_start < input_end:
#     while input_start < input_end + 1:
#         print(input_start)
#         input_start += 1
# elif input_end < input_start:
#     while input_end < input_start + 1:
#         print(input_end)
#         input_end += 1

# while True:
#     if input_start > input_end:
#         break
#     print(input_start)
#     input_start += 1
    
for i in range(input_start, input_end):
    print(i)