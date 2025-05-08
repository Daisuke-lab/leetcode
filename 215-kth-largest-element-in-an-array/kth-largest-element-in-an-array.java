class Solution {
    int[] nums;
    public int findKthLargest(int[] nums, int k) {
        this.nums = nums;
        return quickSelect(0, nums.length -1, nums.length - k+ 1);
    }

    public int quickSelect(int left, int right, int k) {
        if (left == right) {
            return nums[left];
        }
        int pivotIndex = getPivot(left, right);
        int pivotNum = nums[pivotIndex];
        nums[pivotIndex] = nums[right];
        nums[right] = pivotNum;
        int i = left;
        int j = right - 1;
        while (true) {
             // [4, 5, 7, 6] pivot = 6
             //        \U0001f446 you want to swap this and pivot
             // But i and j meets at index 1 (num = 5), so You need to conditino i <= j not i < j
            while (i <= j && nums[i] < pivotNum) {
                i++;
            }
            while (i <= j && nums[j] >= pivotNum) {
                j--;
            }
            if (i < j) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j--;
            } else {
                break;
            }
        }
        nums[right] = nums[i];
        nums[i] = pivotNum;
        // System.out.println("pivot Num:" + Integer.toString(pivotNum));
        // System.out.println("i:" + Integer.toString(i));
        if (i == k -1) {
            return pivotNum;
        } else if (i < k - 1) {
            return quickSelect(i+1, right, k);
        } else {
            return quickSelect(left, i-1, k);
        }
        
        

    }

    public int getPivot(int min, int max) {
        Map<Integer, Integer> numMap = new HashMap<>();
        List<Integer> numList = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < 3; i++) {
            int randomIndex = random.nextInt(max - min + 1) + min;
            numMap.put(nums[randomIndex], randomIndex);
            numList.add(nums[randomIndex]);
        }
        Collections.sort(numList);
        int middleNum = numList.get(1);
        return numMap.get(middleNum);
        
    }
}