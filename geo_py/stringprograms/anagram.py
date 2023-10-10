#anagram
text="bread"
out="beard"
sort_text=sorted(text)
sort_out=sorted(out)
if sorted(text)==sorted(out):
    print("anagram")
else:
    print("not anagram")