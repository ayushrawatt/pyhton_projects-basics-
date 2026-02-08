num_pad=((1,2,3),
         (4,5,6),
         ("*",0,"#"))

for rows in num_pad:
    for nums in rows:
        print(nums,end=" ")
    print()
