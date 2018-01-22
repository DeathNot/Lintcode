class Solution {
public:
    int binarySearch(vector<int> &array, int target) {
        int begin = 0, end = array.size();
        int mid = (begin + end) / 2;

        do {
          if (array[mid] >= target)
            end = mid;
          else if (array[mid] < target)
            begin = mid;
          mid = (begin + end) / 2;
        } while (begin < mid);

        if (array[mid] == target)
          return mid;
        else if(array[mid+1] == target)
          return mid + 1;
        else
          return -1;
    }
};
