class Solution {
	//unordered_map<std::pair<string::iterator, string::iterator>, bool> cache;
public:
    string longestPalindrome(string s) {
		string::iterator first = s.begin(), last = s.begin();
		for(auto it = s.begin(); it != s.end(); ++it) {
			for(auto jt = it; jt != s.end(); ++jt) {  // [it,jt]
				if (last - first + 1 >= jt - it + 1)
					continue;
				if (!okay(it, jt))
					continue;
				first = it;
				last = jt;
			}
		}
		return string(first, last+1);
    }
private:
	bool okay(string::iterator first, string::iterator last) {
		int len = last - first + 1;
		if (len <= 0) return false;
		if (len == 1) return true;
		if (len == 2) return first[0] == first[1];

		//if(cache.count({first, last}))
		//	return cache[{first, last}];

		return *first == *last && okay(++first, --last);
		//cache[{first, last}] = *first == *last && okay(++first, --last);
		//return cache[{first, last}];
	}
};