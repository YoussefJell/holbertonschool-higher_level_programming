#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, mode='a', encoding="utf-8") as my_file:
        my_file.write(text)
    return len(text)


nb_characters_added = append_write(
    "file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
