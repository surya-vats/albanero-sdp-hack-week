def encodeString(str):
    map ={}
    res = " "
    i =0
    for ch in str:
        if ch not in map :
            map[ch] = i
            i += 1
        res += str(map[ch])
    return res

def findmatchword(dict,pattern):
    Len = len(pattern)
    hash = encodeString(pattern)

    for word in dict :
        if (len(word) == Len and encodeString(word)==hash ):
            print (word ,end = " ")

dict = ["abb","abc","npp","cyt","xyy","uyt"]
pattern ="stt"
findmatchword(dict,pattern)





