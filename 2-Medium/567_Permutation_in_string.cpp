/*Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
  */

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;
    
        std::vector<int> s1Freq(26, 0), s2Freq(26, 0);
        
        for (int i = 0; i < s1.size(); ++i) {
            s1Freq[s1[i] - 'a']++;
            s2Freq[s2[i] - 'a']++;
        }
        
        if (s1Freq == s2Freq) return true;
        
        for (int i = s1.size(); i < s2.size(); ++i) {
            s2Freq[s2[i] - 'a']++;
            s2Freq[s2[i - s1.size()] - 'a']--;
            
            if (s1Freq == s2Freq) return true;
        }
        
        return false;
    }
};
