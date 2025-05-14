class Solution {
    private Map<Integer, List<Integer>> outList;
    private Map<Integer, List<Integer>> inList;
    private Stack<Integer> zeroIncomings;
    private Set<Integer> visited;
    private List<Integer> answer;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        outList = initOutList(numCourses, prerequisites);
        inList = initInList(numCourses, prerequisites);
        zeroIncomings = initStack();
        visited = new HashSet<>();
        answer = new ArrayList<>();
        while (!zeroIncomings.empty()) {
            int i = zeroIncomings.pop();
            if (findCycle(i, new HashSet<>())) {
                    return new int[0];
                }
        }
        if (answer.size() != numCourses) {
            return new int[0];
    }
        Collections.reverse(answer);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    public boolean findCycle(int curr, Set<Integer> path) {
        //System.out.println(curr);
        if (path.contains(curr)) {
            return true;
        }
        path.add(curr);
        for (int ad: outList.get(curr)) {
            if (findCycle(ad, path)) {
                return true;
            }
        }
        if (!visited.contains(curr)) {
            answer.add(curr);
        }
        path.remove(curr);
        visited.add(curr);
        return false;

    }

    public Stack<Integer> initStack() {
        Stack<Integer> stack = new Stack<>();
        for (int key: inList.keySet()) {
            if (inList.get(key).size() == 0) {
                stack.add(key);
            }
        }
        return stack;
    }

    public Map<Integer, List<Integer>> initInList(int n, int[][] edges) {
        Map<Integer, List<Integer>> adList = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adList.put(i, new ArrayList<>());
        }
        for (int[] edge: edges) {
            adList.get(edge[0]).add(edge[1]);
        }
        return adList;
    }


    public Map<Integer, List<Integer>> initOutList(int n, int[][] edges) {
        Map<Integer, List<Integer>> adList = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adList.put(i, new ArrayList<>());
        }
        for (int[] edge: edges) {
            adList.get(edge[1]).add(edge[0]);
        }
        return adList;
    }
}