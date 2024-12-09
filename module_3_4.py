def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        word = word.lower()
        if root_word in word:
            same_words.append(word)
    return same_words

result_1 = single_root_words("трав", "трава", "травянной", "страх", "отрава", "траулер")
result_2 = single_root_words("мор", "ПоМоры", "поМидоры", "Мореман")
print(result_1)
print(result_2)
