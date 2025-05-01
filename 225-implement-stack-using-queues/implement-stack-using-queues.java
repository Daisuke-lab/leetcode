class MyStack {
    private Queue<Integer> queue;
    public MyStack() {
        this.queue = new LinkedList<>();
    }
    
    public void push(int x) {
        queue.add(x);
    }
    
    public int pop() {
        Queue<Integer> newQueue = new LinkedList<>();
        int temp = 0;
        while (!queue.isEmpty()) {
            temp = queue.poll();
            if (!queue.isEmpty()) {
                newQueue.add(temp);
            }
        }
        queue = newQueue;
        return temp;
    }
    
    public int top() {
        int temp = pop();
        queue.add(temp);
        return temp;
    }
    
    public boolean empty() {
        return queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */