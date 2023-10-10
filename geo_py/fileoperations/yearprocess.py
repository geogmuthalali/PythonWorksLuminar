path1="C:\\Users\\GEO\\Desktop\\geo_py\\fileoperations\\year.txt"
path2="C:\\Users\\GEO\\Desktop\\geo_py\\fileoperations\\lyear.txt"
f_read=open(path1,"r")
l_write=open(path2,"w")

for year in f_read:
    year=int(year)

    if(year%100==0) and (year %400==0):
        l_write.write(str(year)+"\n")
    elif(year%100!=0) and (year %4==0):
        l_write.write(str(year)+"\n")    
# [l_write.write(str(year)+"\n") for year in f_read if int(year)%4==0 ]