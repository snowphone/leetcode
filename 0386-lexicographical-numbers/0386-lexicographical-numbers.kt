class Solution {
    fun lexicalOrder(n: Int): List<Int> {
        val answer = mutableListOf<Int>()

        for (i in 1..9) {
            if (i <= n) {
                answer.add(i)
                this.generate(i.toString(), n, answer)
            }
        }
        return answer
    }

    private tailrec fun generate(prefix: String, limit: Int, answer: MutableList<Int>) {
        for (i in 0..9) {
            val candidate = "${prefix}${i}"
            val candidate_num = candidate.toInt()

            if (candidate_num <= limit) {
                answer.add(candidate_num)
                this.generate(candidate, limit, answer)
            }
        }
    }
}