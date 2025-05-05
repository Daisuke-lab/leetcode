class Node {
    public int distance;
    public int i;
    public Node(int distance, int i) {
        this.distance = distance;
        this.i = i;
    }
}

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Node> maxHeap = new PriorityQueue<>((obj1, obj2) -> obj2.distance - obj1.distance);
        int[][] answer = new int[k][2];
        for (int i=0; i < points.length; i++) {
            int distance = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            if (maxHeap.size() >= k && maxHeap.peek().distance > distance) {
                maxHeap.poll();
                maxHeap.add(new Node(distance, i));
            } else if (maxHeap.size() < k) {
                maxHeap.add(new Node(distance, i));
            }
        }
        for (int i=k-1; i >= 0; i--) {
            answer[i] = points[maxHeap.poll().i];
        }
        return answer;
    }
}