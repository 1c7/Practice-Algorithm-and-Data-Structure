# grokking algorithem, page 100, chapter 6, breadth-first search
# scenrio: you are a proud owner of mongo farm, trying to find a mongo seller
# who can sell you mongo

from collections import deque
# deque mean double-end queue

graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom','jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = ['seller']


def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []  # prevent infinite loop
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        print( person + "is mongo seller!")
	return True
      else:
        search_queue += graph[person]
	searched.append(person)
  return False

def person_is_seller(person):
  return person == 'seller'

print( search('you') )








