class Solution {
    // get path
    // remove the vertices that is not a part of cycle => get the cycle
    // hashmap = {value: index in path} so that once you find the cycle you can start from the index
    // 
    //  check an edge again backward. if edge is a part of cycle, it's redunant connection
    private Set<Integer> visited;
    private Map<Integer, List<Integer>> adList;
    public int[] findRedundantConnection(int[][] edges) {
        adList = initAdList(edges);
        visited = new HashSet<>();
        List<Integer> path = new ArrayList<>();
        Set<Integer> cycle = new HashSet<>();
        int cycleStartingV = dfs(path, cycle, 1, -1);
        //System.out.println(path);
        for (int i=path.size() - 1; i >= 0; i--) {
            int v = path.get(i);
            if (v == cycleStartingV) {
                break;
            } else {
                cycle.remove(v);
            }
        }
        for (int i = edges.length -1; i >= 0; i--) {
            if (cycle.contains(edges[i][0]) && cycle.contains(edges[i][1])) {
                return edges[i];
            }
        }
        return null;

    }

    public int dfs(List<Integer> path, Set<Integer> cycle, int currV, int prevV) {
        if (cycle.contains(currV)) {
            return currV;
        }
        // System.out.println(currV);
        // System.out.println(cycle);
        int result = -1;
        cycle.add(currV);
        visited.add(currV);
        for (Integer ad: adList.get(currV)) {
            if (ad == prevV) {
                continue;
            }
            int childResult = dfs(path, cycle, ad, currV);
            //System.out.println("childResult:" + childResult);
            if (childResult != -1){
                path.add(currV);
                return childResult;
            }
        }
        cycle.remove(currV);
        return -1;
    }

    public Map<Integer, List<Integer>> initAdList(int[][] edges) {
        int n = edges.length;
        Map<Integer, List<Integer>> adList = new HashMap<>();
        for (int i=1; i <= n; i++) {
            adList.put(i, new ArrayList<>());
        }
        for (int[] edge: edges) {
            adList.get(edge[0]).add(edge[1]);
            adList.get(edge[1]).add(edge[0]);
        }
        return adList;
    }
}