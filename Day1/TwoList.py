list1=['A','app','a','d','ke','th','doc','awa']
list2=['y','tor','e','eps','ay',None,'le','n']
s=' '
rev_list2 = list2[::-1]

for i in range(len(list1)):
    if rev_list2[i] == None:
        s+=list1[i]+' '
    else:
        s+=list1[i]+rev_list2[i]+" "
print(s)

