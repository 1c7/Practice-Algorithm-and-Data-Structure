# adjacent list 
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def bfs(graph, start, end):
    queue = []      # maintain a queue of paths
    queue.append([start]) ## push the first path into the queue

    while queue:
        # get the first path from the queue
        path = queue.pop(0) # path == 1
        # get the last node from the path
        node = path[-1] # 1
        # path found
        if node == end: #
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print (bfs(graph, '1', '11'))
# find a path between 1 and 11


print(  graph.get('1', [])  ) 
# 这个 dict 的 get 方法是什么意思?
