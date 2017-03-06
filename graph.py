import Queue as Q
class Vertex:
    def __init__(self,key,i):
        self.key = key # ususally the weight to get to that vertex
        self.id = i

    def __ge__(self,other):
        return self.key > other.key
    def __eq__(self,other):
        return (self.key,self.id) == (other.key,other.id)
    def __ne__(self,other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash((self.id, self.key))

    def __str__(self):
        return str((self.id, self.key))

class Graph:
    def __init__(self):
        self.ids = 0 # number of vertices
        self.data={} # adjacency list

    def neighbors(self,vid):
        return self.data[vid]

    def addVertex(self,key):
        v = Vertex(key,self.ids)
        self.data[v] = []
        self.ids +=1
        return v

    def addEdge(self,v1,v2):
        self.data[v1].append(v2)
    def doublEdgedSword(self,v1,v2):
        self.data[v1].append(v2)
        self.data[v2].append(v1)

    def path(self,v1, v2):
        pred = [-1 for i in range(self.ids)]  # to recover path
        # initalize distance array
        d = [-1 for i in range(self.ids)]
        pq = Q.PriorityQueue()
        d[v1.id] = v1.key
        pq.put((d[v1.id],v1)) # priority queue based on distance from v1
        gotWhereIwant = False

        while(not pq.empty() and (not gotWhereIwant)):
            v = pq.get()[1]

            for n in self.data[v]:
                if d[n.id] == -1 or ((d[v.id] + n.key) < d[n.id]):
                    d[n.id] = d[v.id] + n.key
                    pred[n.id] = v
                    pq.put((d[n.id],n))
                if n == v2:
                    gotWhereIwant = True
                    break
        # pred can be used to recover path -  but no need
        return d[v2.id]

    def all_path(self,v1):
        # could be done very differently and more efficiently
        pred = [-1 for i in range(self.ids)]  # to recover path
        # initalize distance array
        d = [-1 for i in range(self.ids)]
        pq = Q.PriorityQueue()
        d[v1.id] = v1.key
        pq.put((d[v1.id],v1)) # priority queue based on distance from v1
        gotWhereIwant = False

        while(not pq.empty() and (not gotWhereIwant)):
            v = pq.get()[1]

            for n in self.data[v]:
                if d[n.id] == -1 or ((d[v.id] + n.key) < d[n.id]):
                    d[n.id] = d[v.id] + n.key
                    pred[n.id] = v
                    pq.put((d[n.id],n))
        # pred can be used to recover path -  but no need
        return d
