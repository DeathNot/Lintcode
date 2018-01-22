class Solution {
public:
    void rotateString(string &str, int offset) {
      string result = str;
      for (int i = 0; i < str.size(); i++) {
        int j = (i + offset) % str.size();
        result[j] = str[i];
      }
      str = result;
    }
};
