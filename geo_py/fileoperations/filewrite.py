               # write

# fw=open("C:\\Users\\Admin\\Desktop\\geo_py\\fileoperations\\fwrite.txt","w")
# fw.write("hi")

# year
#1800-2025
fw=open("C:\\Users\\Admin\\Desktop\\geo_py\\fileoperations\\year.txt","w")
for y in range(1800,2020):
    fw.write(str(y)+"\n")
    
    #
    # read from year.txt  r
    # write leapyear in a leapyear w
    # write non leapyear into non leapyear