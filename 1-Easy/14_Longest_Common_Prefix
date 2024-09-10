//Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix;

        if(strs.size() == 1)
        {
            prefix = strs[0];
        }
        else
        {
            for (int i = 0; i < strs.size() - 1; i++)
            {
                string s1 = strs[i];
                string s2 = strs[i + 1];
                string prefixaux;

                bool same = true;

                for (int j = 0; j < s1.length() && j < s2.length() && same; j++)
                {
                    if (i == 0)
                    {
                        if (s1[j] == s2[j])
                        {
                            prefixaux += s1[j];
                        }
                        else
                        {
                            same = false;
                        }
                    }
                    else
                    {
                        if (s1[j] == s2[j] && s1[j] == prefix[j])
                        {
                            prefixaux += s1[j];
                        }
                        else
                        {
                            same = false;
                        }
                    }
                }
                prefix = prefixaux;
                prefixaux.clear();
            }
        }
        return prefix;
    }
};