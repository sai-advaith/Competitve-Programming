class Solution {
    
    public int calPoints(String[] ops) {
        int S [] = new int[ops.length];
        int top = -1;
        int sum = 0;
        int val = 0;
        for (String s : ops)
        {
            char ch = s.charAt(s.length()-1);
            if (Character.isDigit(ch))
            {
                val = Integer.parseInt(s);
                S[++top] = val;
                sum = sum + val;
            }
            if (ch == 'C')
            {
                val = S[top--];
                sum = sum - val;
            }
            if (ch == 'D')
            {
                val = S[top]*2;
                S[++top] = val;
                sum += val;
            }
            if(ch == '+')
            {
                val = S[top] + S[top-1];
                S[++top] = val;
                sum = sum + val;
            }
        }
        return sum;
    }
}