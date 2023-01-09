Gl = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
Sl = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ь"]
def task(word):
    res = ""
    for sim in word.lower():
        if sim in Gl:
           res+="0"
        else:
            res +="1"
    return res

def check_star(template,word):
    if "?" in template:
        res = []
        stack ={template}
        while stack:
            s = stack.pop()
            if "?" in s:
                stack.add(s.replace("?","1",1))
                stack.add(s.replace("?","0",1))
            else:
                res.append(s)
        for st in res:
            if st in word:
                return True
        return False
    else:
        return template in word

def cadaver(template, word):
    word = task(word)
    i, j =0,0
    while i<len(template) and j<len(word):
        if template[i] == "?":
            i+=1
            j+=1
        elif template[i] == "*":
            return check_star(template[i+1:],word[j:])
        elif template[i] != word[j]:
            return False
        i+=1
        j+=1
    return i==j

print(cadaver(template = "*", word = "отруби"))
