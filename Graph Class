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
       
    def adjacent(self,v):
        return self.vertices[v]
        
    def add_edge(self,v1,v2, s):
        self.vertices[v1].append(v2)
        edge_attributes[(v1,v2)] = {}
        edge_attributes[(v1,v2)]['sound'] = s
