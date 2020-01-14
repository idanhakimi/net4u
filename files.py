#‘r’ – Read mode which is used when the file is only being read
#‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
#‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
#‘r+’ – Special read and write mode, which is used to handle both actions when working with a file


filename = "C:/Users/אידן חכימי/Desktop/hello.txt"
file = open(filename, "w")
file.write("192.168.1.1\n192.168.1.2")
file.close()

file = open(filename, "r")
for line in file:
    print(line)
file.close()







# new_list=list(file.read().splitlines())
# print(type(new_list))
#
# file.close()
# #
# print(new_list)
# for i in new_list:
#     print(i)