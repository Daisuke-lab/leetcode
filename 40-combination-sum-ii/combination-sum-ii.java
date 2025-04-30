class Solution {
    List<List<Integer>> answers;
    int[] candidates;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        answers = new ArrayList<>();
        Arrays.sort(candidates);
        this.candidates = candidates;
        recursion(0, target, new ArrayList<>());
        return answers;
    }
    public void recursion(int i, int target, List<Integer> curr) {
        if (target == 0) {
            answers.add(new ArrayList<>(curr));
            return;
        } else if (target < 0) {
            return;
        } else if (i == candidates.length) {
            return;
        } else {
            curr.add(candidates[i]);
            recursion(i+1, target - candidates[i], curr);
            curr.removeLast();
            while (i + 1 < candidates.length && candidates[i] == candidates[i+1]) {
                i++;
            }
            recursion(i+1, target, curr);
        }
    }
}