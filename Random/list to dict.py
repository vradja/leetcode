lst = ["yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes",
       "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes",
       "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes", "yes",
       "yes", "yes", "yes", "yes", "yes", "yes", "with company"]
# lst = str1.replace(",", "").split('sweet')

dct = {i: lst.count(i) for i in set(lst)}
print(dct)

count = 0
for key, val in dct.items():
    count += val

print("Total = ", count)
