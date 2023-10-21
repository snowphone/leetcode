class Solution {
    public void rotate(int[][] matrix) {
        var n_row = matrix.length;
        var n_col = matrix[0].length;

        transpose(matrix);

        for (int r = 0; r < n_row; r++) {
            reverse(matrix[r]);
        }
    }

    private void reverse(int[] list) {
        var n = list.length;
        var l = 0;
        var r = n - 1;
        while (l < r) {
            var tmp = list[l];
            list[l] = list[r];
            list[r] = tmp;

            l++;
            r--;
        }
    }

    private void transpose(int[][] matrix) {
        var n_row = matrix.length;
        var n_col = matrix[0].length;

        for (int r = 0; r < n_row; r++) {
            for (int c = r + 1; c < n_col; c++) {
                var tmp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = tmp;
            }
        }
    }
}