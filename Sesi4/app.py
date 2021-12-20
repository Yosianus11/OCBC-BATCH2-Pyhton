# file = open("test.txt")
# file.close()

# try:
#    f = open("test.txt", encoding = 'utf-8')
#    # perform file operations
#    f.read(4)

# finally:
#    f.close()

# with open("test.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")

# f = open("test.txt",'r',encoding = 'utf-8')

# print(f.read(12))
# print(f.seek(50))
# print(f.read(4))
# print(f.tell())


# f.seek(0)   # bring file cursor to initial position
# for line in f:
#   print(line, end = '')

# f.seek(0)
# print(f.readline())

# f.close()


# with open('test.txt', 'r') as reader:
#      # Read & print the entire file

#      our_row = reader.readline()
#      print(len(our_row))
#      print(our_row[6],our_row[5])

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# x = 22
# assert x== 20 or x==21, "x harus 20 atau 21"

# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."
# assert ('win32' in sys.platform), "This code runs on Windows only."

# def perkalian_0(num1):
#     return 0* num1 +1

# a =0
# sepuluh_kali_0 = perkalian_0(10)

# assert sepuluh_kali_0 == 0, "bukan nol"
# import sys
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('win32' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
#     print('Windows function was not executed')

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
