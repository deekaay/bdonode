def canVisitAllNodes(arr, X, n):
    q = []
    visited = [False]*n
    q.append(X)
    visited[X] = True
    count = 0
     
    # Loop to implement BFS
    while(len(q) > 0):
        size = len(q)
         
        for i in range(size):
            curr = q.pop(0)
             
            count = count + 1
             
            for j in arr[curr]:
                if(visited[j] == False):
                    q.append(j)
                    visited[j] = True
     
    # Check if all nodes are visited
    if(count == n):
        return True
     
    return False

def townExists(lst):
    townList = [1]
    return len([value for value in lst if value in townList]) > 0

def intersection(lst1, lst2):
    print("    " + str(lst1))
    print("    " + str(lst2))
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


g = open("../data/nodeids.csv")

nodeIdBuf = g.readlines()
nodeIds = [ ]
for x in nodeIdBuf:
    nodeIds.append(x.replace("\n", ""))    

g.close()

import json
j = open("../data/links.json")
links = json.load(j)


for i in range(5,10):

    f = open("products/" + str(i) + ".csv","r")
    lines = f.readlines()
    h = open("products/" + str(i+1) + ".csv", "w")



    for line in lines:
        arr2 = map(lambda l: int(l), line.replace("\n", "").split(","))
        qq = 1
        while (arr2[len(arr2)- qq] < 0 and qq < len(arr2) ):
            q = q+1;
        lastnode = int(arr2[len(arr2)-qq])
        print(lastnode);
        appendNodes = [s for s in nodeIds if int(s) > int(lastnode) ]
        for v in appendNodes:
            arr = list(arr2)
            arr.append(int(v))
            print("Evaluating: " + str(v) )
            print(str(arr))

            if not townExists(arr):
                print(" Town does not exist in " + str(arr))
                continue

            print(" Town exists!")
            print("Condensing links")
            condensedLinks = [ ]
            for vv in arr:
                #loop through arr to get our condensed links
                if (links.get(str(vv)) ):
                    intered = map(lambda l: arr.index(l), intersection(links[str(vv)], arr))
                    print(" Intersection of links: " + str(intered))
                else:
                    intered = [ ]
                #intersection(links[str(vv)], arr).map(lambda x : arr.index(x))
                condensedLinks.append(intered)
            print("Condensed links: " + str(condensedLinks))
            ok = False
            ok = canVisitAllNodes(condensedLinks, int(arr[0]), len(arr))
            print(str(ok))
            if (ok):

                h.write(line.replace("\n","") )
                h.write(",")
                h.write(v + "\n") 
                print (" ok")
            else:
                print (" Not ok")

    f.close()
    h.close()