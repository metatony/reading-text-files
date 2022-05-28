def read_file_content(filename):
    file_content = open("filename, "r")
    data = file_content.read()
    return data


print(read_file_content("story.txt"))


def count_words():
    text = read_file_content("story.txt")
    count = dict()
    words = text.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


print(count_words())
