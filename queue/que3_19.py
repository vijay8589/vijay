# queue implimentation in using class

import collections
q = collections.deque()
print(q)
q.appendleft(10) # use the appendleft method to add the elements in the list
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
q.appendleft(50)
print(q)

q.popleft() # popleft is used to remove the fisr element of the list
q.popleft()
print(q)
q.popleft()
print(q)
q.popleft()
print(q)
q.popleft()
print(q)



