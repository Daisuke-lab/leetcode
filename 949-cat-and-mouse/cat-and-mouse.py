class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = max( map(max,graph) )

		# outDegree of state nodes in game graph.
        gameOutDegree = defaultdict(int)
        for a in range(N+1):
            for b in range(N+1):
                gameOutDegree[(a,b,1)] = len(graph[a])
                gameOutDegree[(a,b,2)] = len(graph[b]) - (1 if 0 in graph[b] else 0)
        
        options = defaultdict(set) # will store possible outcomes for each state: one of {1}, {2}, or {1,2}
        
        invGraph = [[] for _ in range(N+1)]
        for a in range(N+1):
            for na in graph[a]: invGraph[na].append(a)

        res = defaultdict(int)
        leaves = deque()
        for b in range(1,N+1): 
            res[(0,b,2)] = 1
            leaves.append((0,b,2))
        for i in range(1,N+1): 
            res[(i,i,1)] = 2
            leaves.append((i,i,1))
            res[(i,i,2)] = 2
            leaves.append((i,i,2))        
        
        while leaves:
            a,b,t = leaves.popleft()
            r = res[(a,b,t)]
		    
		    #if mouse moves now, then in preceeding state cat moved.
            if t==1: 
                for prevb in invGraph[b]:
                    prevState = (a,prevb,2)
                    if prevb == 0 or prevState in res: continue
                    options[prevState].add(r) #prevState may lead to outcome r
                    gameOutDegree[prevState] -= 1
                    # we can process prevState if r==2 (cat already can win prevState by following prevState -> (a,b,t))
                    # or if we already processed all possible branches from prevState
                    if gameOutDegree[prevState] == 0 or r==2:
                        res[(prevState)] = max(options[prevState])
                        leaves.append( prevState )            
            if t==2:
                for preva in invGraph[a]:
                    prevState = (preva,b,1)
                    if prevState in res: continue
                    options[prevState].add(r)
                    gameOutDegree[prevState] -= 1
                    if gameOutDegree[prevState] == 0 or r==1: 
                        res[(prevState)] = min(options[prevState])
                        leaves.append(prevState)
        return res[(1,2,1)]