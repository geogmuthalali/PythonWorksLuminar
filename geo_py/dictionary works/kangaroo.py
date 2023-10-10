#kangaroo word
source_word="chicken"
target_word="hen"
source_word_lst=[]
kangaro_string=""
for ch in source_word:
    source_word_lst.append(ch)
for ch in target_word:
    if ch in source_word_lst:
        source_word_lst.pop(source_word_lst.index(ch))
        kangaro_string+=ch
print(kangaro_string==target_word)        