class Solution {
    public List<Integer> transformArray(int[] arr) {
        int[] answer = arr.clone();
        
        for (int i = 1; i < arr.length - 1; ++i) {
            if (arr[i-1] < arr[i] && arr[i] > arr[i+1])
                answer[i] -= 1;
            if (arr[i-1] > arr[i] && arr[i] < arr[i+1])
                answer[i] += 1;
        }
        
        return Arrays.equals(arr, answer) ? Arrays.stream(answer).boxed().toList() : transformArray(answer);
    }
}
