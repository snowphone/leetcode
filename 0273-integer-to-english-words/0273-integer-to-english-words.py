class Solution:
    def numberToWords(self, num: int) -> str:
        words = self._solve(num)
        while len(words) > 1 and words[-1] == 'Zero':
            words.pop()
        return ' '.join(words)
    
    def _solve(self, num) -> list[str]:
        if num < 20:
            return [
                {
                0: "Zero",
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen",
                }[num]
            ]
        elif num < 100:
            return [
                {
                    2: "Twenty",
                    3: "Thirty",
                    4: "Forty",
                    5: "Fifty",
                    6: "Sixty",
                    7: "Seventy",
                    8: "Eighty",
                    9: "Ninety",
                } [num // 10],
                *self._solve(num % 10),
            ]
        mapping = {
            100: "Hundred",
            1_000: "Thousand",
            1_000_000: "Million",
            1_000_000_000: "Billion",
            1_000_000_000_000: "Trillion",
        }
        max_n, word = next( (n, w) for n, w in reversed( mapping.items() ) if n <= num )
        return [
            self.numberToWords(num // max_n),
            word,
            self.numberToWords(num % max_n),
        ]