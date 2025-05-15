class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<Integer[]>> outList = initOutList(times, n);
        int maxDistance = 0;
        int[] djList = new int[n+1];
        Arrays.fill(djList, Integer.MAX_VALUE);
        PriorityQueue<Integer[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        Set<Integer> visited = new HashSet<>();
        Integer[] startingPoint = {0, k};
        minHeap.add(startingPoint);
        while (!minHeap.isEmpty()) {
            Integer[] currPoint = minHeap.poll();
            int distance = currPoint[0];
            int currV = currPoint[1];
            if (visited.contains(currV)) {
                continue;
            }
            djList[currV] = distance;
            maxDistance = Math.max(distance, maxDistance);
            visited.add(currV);
            for (Integer[] point: outList.get(currV)) {
                if (!visited.contains(point[1])) {
                    int newDistance = distance + point[0];
                    Integer[] updatedPoint = {newDistance, point[1]};
                    minHeap.add(updatedPoint);
                }
            }
        }
        //System.out.println(visited);
        if (visited.size() == n) {
            return maxDistance;
        } else {
            return -1;
        }

    }

    public Map<Integer, List<Integer[]>> initOutList(int[][] edges, int n) {
        Map<Integer, List<Integer[]>> outList = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            outList.put(i, new ArrayList<>());
        }
        for (int[] edge: edges) {
            int src = edge[0];
            int dest = edge[1];
            int weight = edge[2];
            Integer[] pair = {weight, dest};
            outList.get(src).add(pair);   
        }
        return outList;
    }
}