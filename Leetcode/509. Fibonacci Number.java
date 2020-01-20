class Solution {
    public int fib(int N) {
        int r = 0;
        int j =0;
        int k = 1;
        if (N==0)
            return 0;
        else if (N==1)
            return 1;
        else
        {
            for(int i = 2;i<=N;i++)
            {
                r = j + k;
                j=k;    
                k=r;
            }
            return r;
        }
    }
}