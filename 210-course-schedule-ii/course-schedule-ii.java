class Solution {
    private Map<Integer, List<Integer>> adList;
    private List<Integer> answer;
    private Set<Integer> visited;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        adList = initAdList(numCourses, prerequisites);
        visited = new HashSet<>();
        answer = new ArrayList<>();
        for (int i=0; i < numCourses; i++) {
            if (!visited.contains(i)) {
                if (findCycle(i, new HashSet<>())) {
                    return new int[0];
                }
            }
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
        for (int ad: adList.get(curr)) {
            if (findCycle(ad, path)) {
                return true;
            }
        }
        adList.put(curr, new ArrayList<>());
        if (!visited.contains(curr)) {
            answer.add(curr);
        }
        path.remove(curr);
        visited.add(curr);
        return false;

    }

    public Map<Integer, List<Integer>> initAdList(int n, int[][] edges) {
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