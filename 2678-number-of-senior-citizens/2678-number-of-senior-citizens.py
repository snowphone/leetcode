import re

class Solution:
    pattern = re.compile(r"(\d{10})([MFO])(\d{2})(\d{2})")

    def countSeniors(self, details: List[str]) -> int:
        citizens = map(self._parse, details)

        return sum(1 for citizen in citizens if citizen["age"] > 60)
    
    def _parse(self, detail: str):
        phone_no, gender, age, seat = self.pattern.match(detail).groups()

        return {
            "phone": phone_no,
            "gender": gender,
            "age": int(age),
            "seat": int(seat),
        }
        