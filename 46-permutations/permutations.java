class Solution {
    private List<List<Integer>> permutations;
    private int[] nums;
    public List<List<Integer>> permute(int[] nums) {
        permutations = new ArrayList<>();
        this.nums = nums;
        backtrack(new ArrayList<>());
        return permutations;
    }

    public void backtrack(List<Integer> curr) {
        if (curr.size() == nums.length) {
            permutations.add(new ArrayList<>(curr));
        } else {
            for (int num: nums) {
                if (!curr.contains(num)) {
                    curr.add(num);
                    backtrack(curr);
                    curr.remove(curr.size() - 1);
                }
            }
        }
    }
}