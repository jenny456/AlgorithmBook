def enter_edges(a,b):
    al[a].append(b)
    il[b]=il[b]+1
    


n=int(input("enter the number of nodes: "))
al=[[] for i in range(n)]
il=[0 for i in range(n)]
visited=[False for i in range(n)]
q=[]
enter_edges(5,0)
enter_edges(5,2)
enter_edges(4,0)
enter_edges(4,1)
enter_edges(2,3)
enter_edges(3,1)




for i in range(n):
    if il[i]==0:
        q.append(i)
        visited[i]=True

k=0
while len(q)!=0:
    k=k+1
    temp=q
    q=[]
    for j in temp:
        for i in al[j]:
            il[i]=il[i]-1
    for i in range(n):
        if il[i]==0 and visited[i]==False:
            q.append(i)
            visited[i]=True

print(k)
    



