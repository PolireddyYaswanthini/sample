from collections import defaultdict
visited=[]
l=[]
def bfs(graph,start,search):
    visited=[]
    queue=[start]
    while queue:
        if search not in visited:
          node=queue.pop(0)
          if node not in visited:
            print(node,end=" ")
            visited.append(node)
            for j in graph[node]:
                if j not in visited:
                    queue.append(j)
    return
def search(search):
    if(search in l):
            return True
    if(search not in l):
            return False
graph=defaultdict(list)
i=1
nodes=int(input("enter no. of node"))
while(i<=(nodes-1)):
    v=input("enter the vertex")
    if(i==(nodes-1)):
        k=input("enter neighbor of vertex")
        if v not in l:
            l.append(v)
        if k not in l:
            l.append(k)
            i=i+1
            graph[v].append(k)
    else:
        n=input("enter neighbors of vertex").split(' ')
        for j in n:
           if v not in l:
             l.append(v)
           if j not in l:
               l.append(j)
               i=i+1
               graph[v].append(j)
startnode=input("enter the start node")
searchnode=input("enter the search value")
if graph:
    if startnode in graph:
        if search(searchnode):
            print("element found")
            print("path is")
            bfs(graph,startnode,searchnode)
        else:
            print("element not found")
        


