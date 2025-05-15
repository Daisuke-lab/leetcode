class Solution {
    public int minCostConnectPoints(int[][] points) {
      int mstCost = 0;
      PriorityQueue<Integer[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
      Set<Integer> visited = new HashSet<>();
      Integer[] initPoint = {0, 0};
      minHeap.add(initPoint);
      while (!minHeap.isEmpty()) {
        Integer[] data = minHeap.poll();
        int distance = data[0];
        int i = data[1];
        int[] currPoint = points[i];
        if (visited.contains(i)) {
            continue;
        } 
        visited.add(i);
        mstCost += distance;
        for (int j = 0; j < points.length; j++) {
            if (visited.contains(j)) {
                continue;
            }
            int[] nextPoint = points[j];
            int nextDistance = Math.abs(currPoint[0] - nextPoint[0]) + Math.abs(currPoint[1] - nextPoint[1]);
            Integer[] nextData = {nextDistance, j};
            minHeap.add(nextData);
        }
        
      }
      return mstCost;
    }
}