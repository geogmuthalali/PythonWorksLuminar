# count vowels and consonents in strings
def count_vc(val):
    v_count=0 
    c_count=0
    for ch in range(len(val)):
        if val[ch] in ['a','e','i','o','u']:
            v_count+=1
        else:
            c_count+=1
        print("vowels",v_count)
        print("consonents",c_count)
        
        x=input("enter a string : ")
        count_vc(x)
# word=int(input("enter a word : ")).casefold()
# def vowels_consonents(word):
#     if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
#         print("vowels")
#     else:
#         print("consonents")
        
        