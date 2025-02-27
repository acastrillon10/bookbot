def get_num_words (book_text):
    words = book_text.split()
    return len(words)

def get_characters (book_text):
    characters_dic = {}
    for char in book_text:
        char = char.lower()
        if char in characters_dic:
            characters_dic[char] += 1
        else:
            characters_dic[char] = 1
    return characters_dic

def sorted (counts):
    output = []
    for key, value in counts.items():
        output.append({key:value})
    output.sort(key = lambda x: list(x.values())[0], reverse=True)
    return output

