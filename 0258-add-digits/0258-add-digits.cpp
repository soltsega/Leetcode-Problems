// Technique used: Recursion
// Time complexity: O(logN)
// Space complexity: O(log(logN))


class Solution {
public:
    int addDigits(int n) {
        
        if(n<10)
        return n;
        int total=0;

        while(n>0){
            total += n%10;
            n/=10;
        }
        return addDigits(total);
    }
};