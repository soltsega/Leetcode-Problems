class Solution {
public:
    int addDigits(int n) {
        
        if(n<10)
        return n;
        int total;

        while(n>=0){
            total += n%10;
            n/=10;
        }
        return addDigits(n);
    }
};