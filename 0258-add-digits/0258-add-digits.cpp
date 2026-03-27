class Solution {
public:
    int addDigits(int n) {
        // Base Case: If n is a single digit, we are done
        if (n < 10) {
            return n;
        }

        int total = 0;
        // Sum the digits of the current number
        while (n > 0) {
            total += n % 10;
            n /= 10;
        }

        // Recursively call the function with the NEW sum
        return addDigits(total);
    }
};