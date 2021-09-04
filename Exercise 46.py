def file_word_counter(file_directory):
    word_count = {'word': 0}

    with open(file_directory, 'r') as f:
        file = f.read()
        for word in file.split():
            for key, value in list(word_count.items()):
                count = file.count(word)
                up = {word: count}
                word_count.update(up)

    # sorting from highest to lowest occurency of a word
    sorted_word_count = dict(sorted(word_count.items(), key= lambda item: item[1], reverse= True))

    # print number of words * '*' instead of just a number
    for key, value in sorted_word_count.items():
        if value > 0:
            star = value * '*'
            print(f'{key}: {star}')


if __name__ == '__main__':
    file_word_counter('ex46.txt')

