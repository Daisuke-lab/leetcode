class Solution:
    # Brute Force
    # make a ad list (V + E)
    # starting from every node (V)
    # traverse all the edges
    # O(VE)

    # You don't want the centroid of tree in some cases
    # it's not the middle of tree. it's the middle of coins
    # how do I get farest two coins
    # get the root
    # farest coin - 2
    # what do you want from child=> distance 
    # if -1, -2,  0, => you have to take current one
    # if -1, -1, -1 => you think of it as -1
    # if -2, -1, -1 => you take the max
    # if 3, 4, 5 => you are going to add it 
    # if -1, 2, 3 => you can ignore the negative
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        if len(set(coins)) == 1 and coins[0] == 0:
            return 0
        if n <= 5:
            return 0
        self.coins = coins
        self.ad_list = self.init_ad_list(n, edges)
        edge_node, _,_ = self.get_farest_node(0)
        edge_node2,_,_ = self.get_farest_node(edge_node)
        path = self.get_path(edge_node, edge_node2)
        m = len(path) //2
        root = path[m]
        #print("EDGE NODE:", edge_node, edge_node2, "CENTER:", root)
        #print(path)
        time = self.collect_coins(root)
        if time > 0:
            return time * 2
        else:
            return 0



    def collect_coins(self, node, parent=None):
        curr_time = float("inf")
        found = False
        for ad in self.ad_list[node]:
            if parent == ad:
                continue
            time = self.collect_coins(ad, node) + 1
            # if node == 9:
            #     print("DEBUG:", ad, time)
            # when the coin not found
            if time >= float("inf"):
                continue
            # when you need to add multiple positive numbers
            if time > 0 and curr_time > 0:
                curr_time = curr_time + time if curr_time != float("inf") else time
            # when you see the positive number for the first time
            elif time > 0 and curr_time <= 0:
                curr_time = time 
            # when you only have negative numbers
            elif time <= 0 and (curr_time <= 0 or curr_time == float("inf")):
                curr_time = max(curr_time, time) if curr_time != float("inf") else time
                
        # when you don't find any coin
        if curr_time == float("inf") and self.coins[node] == 1:
            curr_time = -2
        #print("NODE:", node, "TIME:", curr_time)
        return curr_time


    def get_path(self, v1, v2, parent=None):
        if v1 == v2:
            return [v2]
        for ad in self.ad_list[v1]:
            if parent == ad:
                continue
            path = self.get_path(ad, v2, v1)
            if len(path) != 0:
                path.append(v1)
                return path
        return []

    def get_farest_node(self, node, parent=None):
        farest_node = node
        max_distance = 0
        coin_found = False
        for ad in self.ad_list[node]:
            if ad == parent:
                continue
            far_node, distance, coin_found_through = self.get_farest_node(ad, node)
            coin_found = coin_found | coin_found_through
            if max_distance < distance + 1 and coin_found_through:
                farest_node = far_node
                max_distance = distance + 1
        if coin_found is False:
            max_distance = 0
            farest_node = node
        if self.coins[node] == 1:
            coin_found = True
        return farest_node, max_distance, coin_found


    def init_ad_list(self, n, edges):
        ad_list = {i: set() for i in range(n)}
        for v1, v2 in edges:
            ad_list[v1].add(v2)
            ad_list[v2].add(v1)
        return ad_list
        

    