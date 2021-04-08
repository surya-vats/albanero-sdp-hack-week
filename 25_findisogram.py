
def Findisogram(w):
    word = w.lower()
    char_list =[]
    for c in word:
        if c.isalpha():
            if c in char_list:
                return False
            char_list.append(c)
    return True
w = input("Enter any word as string:")
print(Findisogram(w))