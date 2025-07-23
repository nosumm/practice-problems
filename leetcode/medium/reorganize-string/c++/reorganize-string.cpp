#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

string reorganizeString(string s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    
    // Check if rearrangement is possible
    int max_count = 0;
    for (auto& p : freq) {
        max_count = max(max_count, p.second);
    }
    if (max_count > (s.size() + 1) / 2) {
        return "";
    }
    
    // Create a max heap
    priority_queue<pair<int, char>> max_heap;
    for (auto& p : freq) {
        max_heap.push({p.second, p.first});
    }
    
    string result;
    while (max_heap.size() >= 2) {
        auto first = max_heap.top(); max_heap.pop();
        auto second = max_heap.top(); max_heap.pop();
        
        result += first.second;
        result += second.second;
        
        if (--first.first > 0) {
            max_heap.push(first);
        }
        if (--second.first > 0) {
            max_heap.push(second);
        }
    }
    
    if (!max_heap.empty()) {
        result += max_heap.top().second;
    }
    
    return result;
}

int main() {
    vector<string> test_cases = {"aab", "aaab", "a", "aa", "abc", "aabbcc", "aaaaa", "aabb", "aabbb", "aabbbc"};
    
    for (string s : test_cases) {
        string result = reorganizeString(s);
        cout << "Input: " << s << "\nOutput: " << result << "\n\n";
    }
    
    return 0;
}