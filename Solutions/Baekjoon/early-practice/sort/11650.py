N = int(input())
cor_list = [0]*N
print(cor_list)

for i in range(N):
    cor = list(map(int,input().split()))
    cor_list.append(cor)
print(cor_list)
print(len(cor_list))
for i in range(len(cor_list)-1):
    for j in range(len(cor_list)-1):
        if cor_list[j][0] > cor_list[j+1][0]:
            temp = cor_list[j+1]
            cor_list[j+1] = cor_list[j]
            cor_list[j] = temp
        elif cor_list[j][0] == cor_list[j+1][0]:
            if cor_list[j][1] > cor_list[j+1][1]:
                temp = cor_list[j+1]
                cor_list[j+1] = cor_list[j]
                cor_list[j] = temp
print(cor_list)
for i in cor_list:
    print(i[0],i[1])
    


    
