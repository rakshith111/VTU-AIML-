'''
A0* algorithm

'''
class AOStar():
    # instantiate graph object with graph topology, heuristic values, start node
    def __init__(self, graph, heuristicNodeList, startNode):
        self.adjac_list = graph
        self.Heruistics = heuristicNodeList
        self.start = startNode
        self.parent = dict()
        self.status = dict()
        self.solngraph = dict()

    def applyAOStar(self):  # starts a recursive AO* algorithm
        self.aostar(self.start, False)
        self.printsoln()

    def printsoln(self):
        print("FOR THE SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("------------------------------------------------------------")
        print(self.solngraph)
        print("------------------------------------------------------------")

    # Computes the Minimum Cost of child nodes of a given node v
    def computeminimumcostchildnodes(self, node):
        minimumCost = 0
        costToChildNodeListDict = {}
        costToChildNodeListDict[minimumCost] = []
        flag = True
        # iterate over all the set of child node/s
        for nodeInfoTupleList in self.adjac_list.get(node, ''):
            cost = 0
            nodeList = []
            for c, weight in nodeInfoTupleList:
                cost = cost + self.Heruistics.get(c, 0) + weight
                nodeList.append(c)
            if flag == True:  # initialize Minimum Cost with the cost of first set of child node/s
                minimumCost = cost
                # set the Minimum Cost child node/s
                costToChildNodeListDict[minimumCost] = nodeList
                flag = False
            else:  # checking the Minimum Cost nodes with the current Minimum Cost
                if minimumCost > cost:
                    minimumCost = cost
                    # set the Minimum Cost child node/s
                    costToChildNodeListDict[minimumCost] = nodeList
        # return Minimum Cost and Minimum Cost child node/s
        return minimumCost, costToChildNodeListDict[minimumCost]

    def aostar(self, v, backTracking):  # AO* algorithm for a start node and backTracking status flag
        # print("HEURISTIC VALUES :", self.__H)
        # print("SOLUTION GRAPH :", self.__solutionGraph)
        print("PROCESSING NODE :", v)
        print("-----------------------------------------------------------------------------------------")
        # if status node v >= 0, compute Minimum Cost nodes of v
        if self.status.get(v, 0) >= 0:
            minimumCost, childNodeList = self.computeminimumcostchildnodes(v)
            print(minimumCost, childNodeList)
            print()
            self.Heruistics[v] = minimumCost
            self.status[v] = len(childNodeList)
            solved = True  # check the Minimum Cost nodes of v are solved
            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.status.get(childNode, 0) != -1:
                    solved = solved & False
            # if the Minimum Cost nodes of v are solved, set the current node status as solved(-1)
            if solved == True:

                self.status[v] = -1
                self.solngraph[
                    v] = childNodeList  # update the solution graph with the solved nodes which may be a part of solution
            if v != self.start:  # check the current node is the start node for backtracking the current node value
                self.aostar(self.parent[v],
                            True)  # backtracking the current node value with backtracking status set to true
            if backTracking == False:  # check the current call is not for backtracking
                for childNode in childNodeList:  # for each Minimum Cost child node

                    self.status[childNode] = 0
                    self.aostar(childNode,
                                False)  # Minimum Cost child node is further explored with backtracking status as false


h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2}
graph1 = {
    'A': [[('B', 1), ('C', 1)]],
    'B': [[('E', 1)]],
    'C': [[('D', 1)]], }

p = (AOStar(graph1, h1, 'A'))
p.applyAOStar()
