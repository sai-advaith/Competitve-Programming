class Solution {
    public int addDigits(int num) {
        int sum = 0;
        do
        {
            sum = 0;
            while(num>0)
            {
                int r = num%10;
                sum = sum + r;
                num /=10;
            }
            num = sum;
        }while(sum>9);
        return num;
    }
}