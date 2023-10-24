class MaxStack {
	list<int> stk;
	multimap<int, list<int>::iterator> maxstk;
public:
    MaxStack() { }
    
    void push(int x) {
		stk.push_back(x); // O(1)
		maxstk.insert({x, --stk.end()});  // O(log n)
    }
    
    int pop() {
		int item = stk.back();  // O(1)
		stk.pop_back();  // O(1)
		auto it = --maxstk.upper_bound(item);  // O(log n)
		maxstk.erase(it);  // O(log n)
		return item;
    }
    
    int top() {
		return stk.back();  // O(1)
    }
    
    int peekMax() {
		return maxstk.rbegin()->first;  // O(log n)
    }
    
    int popMax() {
		auto it = --maxstk.end();  // O(1)
		auto[elem, stk_it] = *it;  // O(1)

		maxstk.erase(it);  // O(log n)
		stk.erase(stk_it);  // O(1)
		return elem;
    }
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */