class Solution {

public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        auto delta = vector<int>(s.size() + 1);

        for (const auto& shift : shifts) {
            auto l = shift[0], r = shift[1], step = shift[2] == 1 ? 1 : -1;
            delta[l] += step;
            delta[r + 1] -= step;
        }
        int prev = 0;
        for (int i = 0; i < s.size(); ++i) {
            delta[i] += prev;
            s[i] = this->shift(s[i], delta[i]);
            prev = delta[i];
        }
        return s;
    }

private:
    inline char shift(char ch, int step) {
        return ((ch - 'a' + (step % 26) + 26) % 26) + 'a';
    }
};