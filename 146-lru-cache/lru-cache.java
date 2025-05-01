class DoublyLinkedNode {
    public DoublyLinkedNode prev;
    public DoublyLinkedNode next;
    public int key;
    public int val;

    public DoublyLinkedNode() {

    }
}

class LRUCache {
    private int capacity;
    private DoublyLinkedNode head;
    private DoublyLinkedNode tail;
    private Map<Integer, DoublyLinkedNode> nodeMap;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.head = new DoublyLinkedNode();
        this.tail = new DoublyLinkedNode();
        this.head.prev = this.tail;
        this.tail.next = this.head;
        this.nodeMap = new HashMap<>();
        
    }
    
    public int get(int key) {
        if (!nodeMap.containsKey(key)) {
            return  -1;
        } else {
            DoublyLinkedNode node = nodeMap.get(key);
            remove(key);
            insert(key, node);
            return nodeMap.get(key).val;
        }
    }

    public void insert(int key, DoublyLinkedNode node) {
        node.next = head;
        node.prev = head.prev;
        head.prev.next = node;
        head.prev = node;
        nodeMap.put(key, node);
    }
    public void remove(int key) {
        DoublyLinkedNode node = nodeMap.get(key);
        // System.out.println(key);
        // System.out.println(node.val);
        node.prev.next = node.next;
        node.next.prev = node.prev;
        nodeMap.remove(key);
    }
    
    public void put(int key, int value) {
        if (nodeMap.containsKey(key)){
            remove(key);
        } else if (nodeMap.size() == capacity) {
            remove(tail.next.key);
        }
        DoublyLinkedNode node = new DoublyLinkedNode();
        node.val = value;
        node.key = key;
        insert(key, node);
        //System.out.println(nodeMap);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */