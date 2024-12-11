#define max(X, Y) ((X) > (Y) ? (X) : (Y))

int compare(const void *lit, const void *rit) {
  int l = *(int *)(lit);
  int r = *(int *)(rit);

  return l - r;
}

int maximumBeauty(int *nums, int numsSize, int k) {
  qsort(nums, numsSize, sizeof(int), compare);
  int answer = 0;
  int *lit = nums;

  for (int *rit = nums; rit != nums + numsSize; ++rit) {
    while (*lit + k < *rit - k) {
      ++lit;
    }
    answer = max(answer, rit - lit + 1);
  }
  return answer;
}