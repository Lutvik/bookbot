def main():
    book_path = "books/frankenstein.txt"
    text = go_read_a_book(book_path)
    word_num = word_count(text)
    letter_num = character_count(text)
    letter_num_nosp = character_count_alpha(text)
    list_of_dicts = dict_to_list(text)
    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{word_num} words found in the document\n")
    for i in list_of_dicts:
        print(f"The '{i['letter']}' character was found '{i['num']}' times" )
    print("--- End report ---")

def go_read_a_book(book):
    with open(book) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    low_text = text.lower()
    chara_count = {}
    for character in low_text:
        if character in chara_count:
            chara_count[character] += 1
        else:
            chara_count[character] = 1
    return chara_count

def character_count_alpha(text):
    low_text = text.lower()
    chara_count = {}
    for character in low_text:
        if character in chara_count and character.isalpha():
            chara_count[character] += 1
        elif character.isalpha() == False:
            pass
        else:
            chara_count[character] = 1
    return chara_count

def sort_on(dict):
    return dict["num"]

def dict_to_list(text):
    letters_found = character_count_alpha(text)
    list_of_dicts = []
    for i in letters_found:
        num = letters_found[i]
        letter = i
        n_dict = {"letter": letter, "num": num}
        list_of_dicts.append(n_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def character_total(characters):
    total = 0
    for n in characters:
        total += characters[n]
    return total

main()
