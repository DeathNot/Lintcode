class Solution {
public:
    int reverseInteger(int n) {
        long result = 0;
        do {
            int i = n % 10;
            result = result * 10 + i;
            n /= 10;
        } while (n != 0);
        if (result > INT_MAX)
            return 0;
        else
            return result;
    }
};
