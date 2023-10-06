class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            {
                True:                      lambda:  str(i),
                i % 3 == 0:                lambda:  "Fizz",
                i % 5 == 0:                lambda:  "Buzz",
                i % 3 == 0 and i % 5 == 0: lambda:  "FizzBuzz",
            }[True]()
            for i in range(1, n+1)
        ]
