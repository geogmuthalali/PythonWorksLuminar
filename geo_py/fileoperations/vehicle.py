f=open("C:\\Users\\Admin\\Desktop\\geo_py\\fileoperations\\numbers.txt")
all_numbers=[line.rstrip("\n") for line in f]
print(all_numbers)

kerala_nums=[num for num in all_numbers if num.startswith("kl")]
print(kerala_nums)