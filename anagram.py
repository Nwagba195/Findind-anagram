
def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("input word here ")
    anagram = input("input word here ")
    str1 = word.lower()
    str2 = anagram.lower()
    if len(str1) == len(str2) :
    sort_str1 = sorted(str1)
     sort_str2 = sorted(str2)
    
    if sort_str1 == sort_str2 :
     
         return True
    else:
        return False

print(find_anagram('', ''))

