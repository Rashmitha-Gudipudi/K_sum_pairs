list_a=list(map(int,input().split(",")))
pair_sum=int(input())
set_1=set()

for i in range(len(list_a)-1):#0,1,2,3
    num_1=list_a[i]#5 
    num_2=pair_sum-num_1 #12-5=7 
    remain_list=list_a[i+1:]
    if num_2 in remain_list:
        pair=(num_1,num_2)
        sort_e=tuple(sorted(pair))
        set_1.add(sort_e)
    
u_l=list(set_1)
u_l.sort()
for j in u_l:
    print(j)