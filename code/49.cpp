class Solution {
public:
    void sortLetters(string &chars) {
      int begin = 0, end = chars.size() - 1;
      while (begin < end) {
        if (isupper(chars[begin]) && islower(chars[end])) {
          char ch = chars[begin];
          chars[begin] = chars[end];
          chars[end] = ch;
        } else if (islower(chars[begin]))
          begin++;
        else if (isupper(chars[end]))
          end--;
      }
    }
};
