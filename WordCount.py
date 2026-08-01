def count_words(sentence):

    word_count = {}
    sentence_lower_split = sentence.lower().split()
    complete_list = []

    for word in sentence_lower_split:
        clean_word = ""
        for letter in word:
            if letter.isalnum() or letter == "'":
                clean_word = clean_word + letter
            else:
                clean_word = clean_word + " "

        clean_word_strip = clean_word.strip("'")
        split_clean_word = clean_word_strip.split()
        complete_list = complete_list + split_clean_word

    for word in complete_list:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count
