class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subSets = new ArrayList<>();
        subSets.add(new ArrayList<>());
        for (int i=0; i < nums.length; i++) {
            int num= nums[i];
            int currSize = subSets.size();
            for (int j=0; j < currSize; j++) {
                List<Integer> newSubSet = new ArrayList<>(subSets.get(j));
                newSubSet.add(num);
                subSets.add(newSubSet);
            }
        }
        return subSets;
    }
}