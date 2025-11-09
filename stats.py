# Get book and count every word
def word_count(filepath):
    word_count = 0
    with open(filepath) as f:
        text = f.read()
        words = text.split()
        for i in words:
            word_count += 1
    return print(f"Found {word_count} total words")

def get_characters(filepath):
    characters_dict = {}
    with open(filepath) as f:
        text = f.read()
        lower_text = text.lower()
        for w in lower_text:
            if w not in characters_dict:
                characters_dict[w] = 1
            else:
                characters_dict[w] += 1
        return characters_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []
    for i in dict:
        single_dict = {}
        single_dict["char"] = i
        single_dict["num"] = dict[i]
        if str.isalpha(single_dict["char"]):
            dict_list.append(single_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list