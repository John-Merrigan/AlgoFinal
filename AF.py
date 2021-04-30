#!/usr/bin/env python
# coding: utf-8

# # Homework 5 (80 points)

# In this homework, you will learn about:
# 
# * Design and implementation of a Graph library
# * Representation of graphs as adjacency lists
# * Breadth-First Search
# * Depth-First Search
# * Topological Sort
# 
# **Note that I made the deliberate choice of giving you very little instructions about how to design your graph library API. This is on purpose: one of the most important skill for a software engineer is API design. However, note that I will discuss all of this in class, so if you are confused about what you have to do, make sure to tune in. Also note that if you are thoughtful about your design, you will have to write much less code.**

# In[1]:


from math import inf


# You will use the following class to represent vertices in your graph. A vertex has an identifier, and it can also have a set of attributes. An identifier is almost like an attribute, except that it needs to be provided to create a vertex.

# In[2]:


class Vertex:
    
    def __init__(self,id):
        self.attributes = {}
        self.attributes['id'] = id
        
    def __str__(self):
        return str(self.attributes)
        
    def new_copy(self):
        return Vertex(self.attributes['id'])
        
    def set(self,key,value):
        self.attributes[key] = value
        
    def get(self,key):
        return self.attributes[key]


# In[3]:


class Graph:
    
    def __init__(self):
        self.vertices = {}
        self.id_to_v = {}
        self.edge_attributes = {}
    
    def __str__(self):
        s = ''
        for v in self.vertices:
            s += str(v)
            s += '\n\n'
        return s
    
    def add_vertex(self,v):
        self.vertices[v] = []
        self.id_to_v[v.get('id')] = v
    
    def size_vertices(self):
        return len(self.vertices)
    
    def add_edge(self,v1,v2):
        pass
    
    def adjacent(self,v):
        return self.vertices[v]
    
    def BFS(self,start):
        assert(isinstance(start,Vertex))
        result = []
        
        start.set('color','gray')
        start.set('d',0)
        start.set('parent',None)
        
        for v in self.vertices:
            if v == start:
                continue
            
            v.set('color','white')
            v.set('d',inf)
            v.set('parent',None)
        
        queue = []
        queue.append(start)
        
        while len(queue) != 0:
            
            u = queue.pop(0)
            
            for v in self.adjacent(u):
                
                if v.get('color') == 'white':
                    
                    v.set('color','gray')
                    v.set('d',u.get('d') + 1)
                    v.set('parent',u)
                    
                    queue.append(v)
                    
            u.set('color','black')
            result.append(u.get('id'))

        return result
    
    def DFS_Visit(self,u,time):
        
        time += 1
        u.set('d',time)
        u.set('color','gray')
    
        for v in self.adjacent(u):
            
            if v.get('color') == 'white':
                v.set('parent',u)
                time = self.DFS_Visit(v,time)
    
        u.set('color','black')
        time += 1
        u.set('f',time)
    
        return time
    
    def DFS(self):
        
        for v in self.vertices:
            
            v.set('color','white')
            v.set('parent',None)
            
        time = 0
        
        for v in self.vertices:
            
            if v.get('color') == 'white':
                time = self.DFS_Visit(v,time)         


# Your library will provide undirected graphs. Note that you may not change the name of the class, but you can change its inheritance, and you will need to add methods. 

# In[4]:


class UndirectedGraph(Graph):
        
    def add_edge(self,v1,v2):
        self.vertices[v1].append(v2)
        self.vertices[v2].append(v1)


# Likewise, your library will provide directed graphs.

# In[5]:


class DirectedGraph(Graph):
        
    def add_edge(self,v1,v2, s):
        self.vertices[v1].append(v2)
        self.edge_attributes[(v1,v2)] = {}
        self.edge_attributes[(v1,v2)]['sound'] = s 
        
    def transpose(self):
        GT = DirectedGraph()
        
        for v in self.vertices:
            GT.add_vertex(v)
            
        for v in self.vertices:
            for u in self.adjacent(v):
                GT.add_edge(u,v)
        
        return GT
        
    def acyclic(self):
        found_BE = False
        
        for u in self.vertices:
            for v in self.adjacent(u):
                b1 = v.get('d') <= u.get('d')
                b2 = u.get('d') < u.get('f')
                b3 = u.get('f') <= v.get('f')
                if b1 and b2 and b3: 
                    found_BE = True
                    
        return not found_BE
        
    def topological_sort(self):
        self.DFS()
        if self.acyclic():
            result = sorted(self.vertices,key=lambda v: v.get('f'),reverse=True)
            return list(map(lambda v: v.get('id'),result))
        else:
            return None
        
    def checkPath(self, s, verticesTaken, current_vertex):
        #this is crap the try and except shit
        verticesTaken = verticesTaken.append(current_vertex.get('id'))
        if len(s) == 0:
            return verticesTaken 
        #prolly delete current_vertex = self.id_to_v(current_vertex)
        for v in self.adjacent(current_vertex):
            #test print(self.edge_attributes[current_vertex.get('id')]['sound'])
            if self.edge_attributes[(current_vertex,v)]['sound'] == s[0]:
                s = s[1:len(s)]
                current_vertex = v 

                self.checkPath(s, verticesTaken, current_vertex)
    
    def checkPathHelper(self, s, verticesTaken, current_vertex):

        thingToReturn = self.checkPath(s, verticesTaken, current_vertex)
        if thingToReturn == None:
            return 'NO-SUCH-PATH'


# In[ ]:



    


# In[6]:


def create_graph_4():
    G = DirectedGraph()
    
    for i in ['0','1','2','3','4']:
        G.add_vertex(Vertex(i))
        
    for (v1,v2,sigma) in [('0','1','a'),('1','3','b'),('3','4','a'),('0','2','a')]:
        
        G.add_edge(G.id_to_v[v1],G.id_to_v[v2],sigma)
        
    return G


# In[ ]:





# In[7]:


G4 = create_graph_4()
G4.checkPathHelper('aba', [], G4.id_to_v['0'])


# In[ ]:





# In[ ]:





# In[ ]:




