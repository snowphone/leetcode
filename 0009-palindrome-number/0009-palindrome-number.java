class Solution {
    public boolean isPalindrome(int x) {

        var str = String.valueOf(x);

        var rev = new StringBuffer(str).reverse().toString();
        return str.equals(rev);
    }
}