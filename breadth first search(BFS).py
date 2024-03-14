#!/usr/bin/env python
# coding: utf-8

# Breadth First Search

# In[17]:


my_adj={
    'start':['A','B'],
    'A':['start','E','F'],
    'B':['start','D','C'],
    'C':['B'],
    'D':['B','GOAL'],
    'E':['B','G'],
    'F':['B'],
    'G':['E'],
    'GOAL':['E','F']
}


# In[3]:


print(my_adj)


# In[4]:


my_adj


# HANDING QUEUE IN PYTHON:
# operations:
#   1.enqueue
#   2.dequeue
#   3.size
#   4.front
#   5.rear

# In[5]:


from collections import deque


# In[6]:


Q=deque(["a","b","c","d","e"])


# In[7]:


Q.appendleft("0")


# In[8]:


Q


# In[10]:


Q.append("F")


# In[12]:


Q


# In[13]:


Q.popleft()


# In[14]:


Q.pop()


# In[15]:


Q


# In[19]:


Q[0]


# In[20]:


Q[-1]


# In[21]:


len(Q)


# In[14]:


graph={
    'start':['A','B'],
    'A':['start','E','F'],
    'B':['start','D','C'],
    'C':['B'],
    'D':['B','GOAL'],
    'E':['B','G'],
    'F':['B'],
    'G':['E'],
    'GOAL':['E','F']
}


# In[15]:


from collections import deque
def bfs(graph,start,GOAL):
    visited=[]
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
            print("i have visited:",node)
            neighbours=graph[node]
            if node==GOAL:
                return("i have reached the goal,this is my traverse")
            for neighbour in neighbours:
                queue.append(neighbour)


# In[16]:


bfs(graph,"start","GOAL")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




