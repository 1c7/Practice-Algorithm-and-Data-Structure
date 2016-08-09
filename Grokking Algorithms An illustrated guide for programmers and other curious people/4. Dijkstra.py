# dai ke si zhua 

# page 134 grokking algorithem




#graph
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

# cost table
infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# parent table
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# Finally, you need an array to keep track of all the nodes you’ve already
# processed, because you don’t need to process a node more than once:
processed = []


# find in cost table
def find_lowest_cost_node(costs):
  lowest_cost = float('inf')
  lowest_cost_node = None
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node



node = find_lowest_cost_node(costs)
while node is not None:
	cost = costs[node]   # (Number) lowest_cost_node's cost
	neighbors = graph[node]  # (Dict)
	for n in neighbors.keys(): # loop though all neighbors
	  new_cost = cost + neighbors[n]
	  if costs[n] > new_cost:
	  	costs[n] = new_cost
	  	parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)




# correct answer should be: start, b, fin




