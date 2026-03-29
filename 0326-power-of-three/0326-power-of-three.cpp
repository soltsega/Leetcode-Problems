class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<=0){
            return false;
        }
        int pro = 0;
        while(pow(3,pro) <= n){
            if(n==pow(3,pro)){
                return true;
            }
            pro++;
        }
        return false;
        
    }
};