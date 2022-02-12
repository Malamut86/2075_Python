def get_uniq_numbers(src: list):
    pass
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

for i in range(len(src)):
   flag = 1
   for j in range(len(src)):
      if src[i] == src[j] and i != j:
         flag = 0
         break
   if flag:
       print(src[i])
