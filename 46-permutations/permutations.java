class Solution {
    private List<List<Integer>> permutations;
    private int[] nums;
    public List<List<Integer>> permute(int[] nums) {
        permutations = new ArrayList<>();
        this.nums = nums;
        backtrack(new ArrayList<>(), new HashSet<>());
        return permutations;
    }

    public void backtrack(List<Integer> curr, Set<Integer> visited) {
        if (curr.size() == nums.length) {
            permutations.add(new ArrayList<>(curr));
        } else {
            for (int num: nums) {
                if (!visited.contains(num)) {
                    curr.add(num);
                    visited.add(num);
                    backtrack(curr, visited);
                    curr.remove(curr.size() - 1);
                    visited.remove(num);
                }
            }
        }
    }
}