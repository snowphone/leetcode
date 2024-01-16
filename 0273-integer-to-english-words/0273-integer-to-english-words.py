class Solution:
    @cache
    def numberToWords(self, num: int) -> str:
        if num <= 19:
            return {
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
    
        if num < 100:
            tens = {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety",
            }
            answer = tens[num // 10]
            remaining = num % 10
            if remaining == 0:
                return answer
            return f"{answer} {self.numberToWords(remaining)}"
    
        max_separator = {
            3: "Hundred",
            4: "Thousand",
            7: "Million",
            10: "Billion",
            13: "Trillion",
            17: "Quadrillion",
        }
        most_significant_digit_len = max(
            it for it in max_separator.keys() if it <= len(str(num))
        )
        mult = 10 ** (most_significant_digit_len - 1)
    
        max_digit = num // mult
        answer = (
            f"{self.numberToWords(max_digit)} {max_separator[most_significant_digit_len]}"
        )
        remaining = num % mult
        if remaining == 0:
            return answer
        return f"{answer} {self.numberToWords(remaining)}"
    