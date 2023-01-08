
class AOStar():
    # instantiate graph object with graph topology, heuristic values, start node
    def __init__(self, graph, Heruistics, startNode):
        self.maingraph = graph
        self.Heruistics = Heruistics
        self.start = startNode
        self.parent = dict()
        self.status = dict()
        self.result = dict()

    def applyAOStar(self):  # starts a recursive AO* algorithm
        self.aostar(self.start, False)
        self.printsoln()

    def printsoln(self):
        print("FOR THE SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("------------------------------------------------------------")
        print(self.result)
        print("------------------------------------------------------------")
        print("HEURISTIC VALUES OF THE NODES ARE:")
        print(self.Heruistics)

    # Computes the Minimum Cost of child nodes of a given node v

    def mincost(self, node):
        mincostchilds = []
        minimumCost = 0
        for adjnodes in self.maingraph.get(node, ''):
            cost = 0
            weight = 1  # In AOStar  the weight of the child node is 1
            # sum up the heuristic values of the child nodes
            for child in adjnodes:
                cost += self.Heruistics.get(child) + weight
            mincostchilds.append((cost, adjnodes))
        # if there are no child nodes, return 0
        if len(mincostchilds) == 0:
            return 0, []
        else:  # return the minimum cost of child nodes
            minimum = min(mincostchilds)
            minimumCost = minimum[0]
            mincostchilds = minimum[1]
            return minimumCost, mincostchilds

    def aostar(self, v, backTracking):  # AO* algorithm for a start node and backTracking status flag

        print("-----------------------------------------------------------------------------------------")
        print("PROCESSING NODE :", v)
        # if status node v >= 0, compute Minimum Cost nodes of v
        if self.status.get(v, 0) >= 0:
            minimumCost, childNodeList = self.mincost(v)
            self.Heruistics[v] = minimumCost
            self.status[v] = len(childNodeList)
            solved = True
            for childNode in childNodeList:
                self.parent[childNode] = v
                # check the Minimum Cost nodes of v are solved
                if self.status.get(childNode, 0) != -1:
                    # if the Minimum Cost nodes of v are not solved, set the solved flag to false
                    solved = False
            # if the Minimum Cost nodes of v are solved, set the current node status as solved(-1)
            if solved:
                self.status[v] = -1
                self.result[v] = childNodeList
            # if the current node is not the start node, call the AO* algorithm for the parent node
            if v != self.start:
                self.aostar(self.parent[v], True)
    
            if backTracking == False:  # check the current call is not for backtracking
                for childNode in childNodeList:  # for each Minimum Cost child node
                    self.status[childNode] = 0
                    self.aostar(childNode, False)

h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2,
      'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
graph1 = {
    'A': [[('B'), ('C')], [('D')]],
    'B': [[('G')], [('H')]],
    'C': [[('J')]],
    'D': [[('E'), ('F')]],
    'G': [[('I')]]
}
p = (AOStar(graph1, h1, 'A'))
p.applyAOStar()