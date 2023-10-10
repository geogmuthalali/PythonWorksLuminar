from json import load

path="C:\\Users\\GEO\\Desktop\\geo_py\\movies\\mdb.json"
with open(path,encoding="utf-8")as f:
    films=load(f)
# print total number of films
print(len(films))    
# print all movie released in 2015
movie_filter=[f.get("title") for f in films if f.get("year")=="2015"]
print(movie_filter)
# print comedy genres movie title
comedy_films=[f.get("title") for f in films if "Comedy" in f.get("genres")]
print(comedy_films)
#  print id in range(20,30) and runtime>110 
mfilter=[f.get("title") for f in films if f.get("id") in range(20,31) and f.get("runtime")>="110"]
print(mfilter)
#film title must be  one word
title_filter=[f.get("title") for f in films if len(f.get("title").split(" "))==1]
print(title_filter)
#
# text="hai hello"
# print[t.get("text")for t in text if len(t.get("text").split(" ")==1)]
#
# genre=drama runtime=max
drama_films=[f for f in films if "Drama" in f.get("genres")]
lengthy_movie=max(drama_films,key=lambda f:int(f.get("runtime"))) 
print(lengthy_movie)
# print  * genres
# all_genres=[f.get("genres") for f in films if f.get("genres") and f.get("title")]
# print(all_genres)
wc={}
for m in films:
    year=m.get("year")

    if year in wc:
      wc[year]+=1
    else:
       wc[year]=1
          
# print which year most movie are released
# release_films=[f.get("year") for f in films if f.get("year")]
# most_films=max(release_films)
# print(most_films)
out=max(wc,key=lambda k:wc.get(k))
print(out)
# #
# shop={"samsung":10,"apple":20,"redmi":110,"oppo":45}
print(max(v,k) for k,v in wc.items())
