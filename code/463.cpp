class Solution {
public:
    void sortIntegers(vector<int> &A) {
        if (A.size() < 2)
          return;
        for (unsigned int i = 0; i < A.size(); i++) {
          for (unsigned int j = i + 1; j < A.size(); j++) {
            if (A[i] > A[j]) {
              int val = A[i];
              A[i] = A[j];
              A[j] = val;
            }
          }
        }
    }
};
