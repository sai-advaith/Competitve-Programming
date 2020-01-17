class Solution {
    public boolean backspaceCompare(String S, String T) {
        char stack[] = new char[S.length()];
        char stack2[] =new char[T.length()];
        int top = -1;
        int top2 = -1;
        for(int i =0;i<S.length();i++)
        {
            char ch = S.charAt(i);
            if(Character.isAlphabetic(ch))
                stack[++top] = ch;
            if(ch == '#' && top >= 0)
                    stack[top--] = '\u0000';
        }
        for(int i =0;i<T.length();i++)
        {
            char ch = T.charAt(i);
            if(Character.isAlphabetic(ch))
                stack2[++top2] = ch;

            if(ch == '#' && top2 >= 0)
                    stack2[top2--] = '\u0000';
        }

        String s3 = new String(stack);
        String s4 = new String(stack2);
        return (s3.trim()).equals(s4.trim());
    }
}