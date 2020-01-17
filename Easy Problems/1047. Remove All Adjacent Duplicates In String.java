class Solution {
    public String removeDuplicates(String S) {
        char stack[] = new char[S.length()];
        int top = -1;
        for(int i =0;i<S.length();i++)
        {
            char ch = S.charAt(i);

            if(top >= 0 && ch == stack[top])
            {
                stack[top--] = ' ';
                continue;
            }

                stack[++top] = ch;
            
        }   
        String s = new String(stack);
        return s.trim();
    }
}