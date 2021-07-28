def files():
    # Open file for writing and create it if it doesn't exist
#     f = open('text.txt', 'w+')
    # Open file for appending text to the appending
#     f = open('text.txt', 'a')
    # Write some line of data to the file
#     for i in range(10):
#         f.write("This is the line " + str(i) + "\r\n")

#     Open file to read
    f = open('text.txt', 'r')

    # Open the files backend and read the content
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    # Close the files when done
    f.close()

def osUtilities():


if __name__ == '__main__':
    files()