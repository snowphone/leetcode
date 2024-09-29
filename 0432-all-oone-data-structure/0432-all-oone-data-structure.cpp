#include <list>
#include <ostream>
#include <string>
#include <unordered_map>
using namespace std;

typedef std::pair<string, int> Pair;
typedef std::list<Pair>::iterator Iter;

class AllOne {
  std::unordered_map<string, Iter> key_to_iter_map;
  std::list<Pair> sorted_list; // sorted
public:
  void inc(string key) {
    if (key_to_iter_map.find(key) == key_to_iter_map.end()) {
      sorted_list.push_front({key, 0});
      auto it = sorted_list.begin();
      key_to_iter_map[key] = it;
    }
    auto it = this->key_to_iter_map[key];
    it->second++;

    auto not_sorted = [this](const string &key) {
      auto it = this->key_to_iter_map[key];
      auto nxt = std::next(it);
      return (nxt != this->sorted_list.end() && it->second > nxt->second);
    };

    while (not_sorted(key)) {
      auto it = this->key_to_iter_map[key];
      this->swap(it, std::next(it));
    }
  }

  void dec(string key) {
    auto it = this->key_to_iter_map[key];
    it->second--;

    auto not_sorted = [this](const string &key) {
      auto it = this->key_to_iter_map[key];
      return (it != sorted_list.begin() && it->second < std::prev(it)->second);
    };

    while (not_sorted(key)) {
      auto it = this->key_to_iter_map[key];
      this->swap(it, std::prev(it));
    }

    it = this->key_to_iter_map[key];
    if (it->second == 0) {
      this->sorted_list.erase(it);
      this->key_to_iter_map.erase(key_to_iter_map.find(key));
    }
  }

  string getMaxKey() {
    if (this->sorted_list.empty()) {
      return "";
    }
    return this->sorted_list.back().first;
  }

  string getMinKey() {
    if (this->sorted_list.empty()) {
      return "";
    }
    return this->sorted_list.front().first;
  }

private:
  void swap(Iter it1, Iter it2) {
    std::iter_swap(it1, it2);
    this->key_to_iter_map[it1->first] = it1;
    this->key_to_iter_map[it2->first] = it2;
  }
};
