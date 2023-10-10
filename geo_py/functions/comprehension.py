# list comprehension
lst=[4,5,6,7,8,2,1]
# squares=[]
# for n in lst:
#     squares.append(n**2)

squares=[n**2 for n in lst] 
print(squares) 
cubes=[n**3 for n in lst]
print(cubes)
# odd or even
odds=[n for n in lst if n%2==0]
print(odds)
evens=[n for n in lst if n%2!=0]
print(evens)
num_gtfive=[n for n in lst if n>=5]
print(num_gtfive)
#
# years
years=[y for y in range(1800,2025)]
print(years)
century_year=[y for y in years if y%100==0]
print(century_year)
noncentury_years=[y for y in years if y%100!=0]
print(noncentury_years)