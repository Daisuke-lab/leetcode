class Node {
    public int frequency;
    public char c;
    public Node(char c) {
        this.frequency = 1;
        this.c = c;
        
    }
}
class Solution {
    public String frequencySort(String s) {
        PriorityQueue<Node> maxHeap = new PriorityQueue<>((obj1, obj2) -> obj2.frequency - obj1.frequency);
        Map<Character, Node> countMap = new HashMap<>();
        for (int i=0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (countMap.containsKey(c)) {
                countMap.get(c).frequency++;
            } else {
                countMap.put(c, new Node(c));
            }
        }
        countMap.keySet().forEach((Character c) -> maxHeap.add(countMap.get(c)));
        StringBuilder str = new StringBuilder();
        while (!maxHeap.isEmpty()) {
            Node node = maxHeap.poll();
            for (int i = 0; i < node.frequency; i++) {
                str.append(node.c);
            }
            //str.append(node.c * node.frequency);
        }
        return str.toString();
        
    }
}