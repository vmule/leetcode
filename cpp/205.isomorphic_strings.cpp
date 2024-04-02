#include <string>
#include <unordered_map>
#include <vector>

class Solution {
 public:
    bool isIsomorphic(std::string s, std::string t) {
        std::unordered_map<char, int> mapS;
        std::unordered_map<char, int> mapT;

        std::vector<int> listS;
        std::vector<int> listT;

        for (int i = 0; i < s.size(); ++i) {
            if (mapS.contains(s[i])) {
                listS.push_back(mapS[s[i]]);
            } else {
                mapS[s[i]] = i;
                listS.push_back(mapS[s[i]]);
            }

            if (mapT.contains(t[i])) {
                listT.push_back(mapT[t[i]]);
            } else {
                mapT[t[i]] = i;
                listT.push_back(mapT[t[i]]);
            }
        }

        for (int i = 0; i < listS.size(); ++i) {
            if (listS[i] != listT[i]) {
                return false;
            }
        }

        return true;
    }
};
