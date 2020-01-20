class Solution {
    public boolean detectCapitalUse(String word) {
        boolean g = true; // upper
        boolean f = true; // lower
        boolean h = true; // starts with upper
        for (int i =0 ;i <word.length();i++)
        {
            if(!Character.isUpperCase(word.charAt(i)))
                g = false;   
        }
        for (int i =0 ;i < word.length(); i++)
        {
            if(!Character.isLowerCase(word.charAt(i)))
                f = false;
        }
        h = Character.isUpperCase(word.charAt(0));
        for (int i =1 ;i <word.length();i++)
        {
            if(!Character.isLowerCase(word.charAt(i)))
                h = false;
        }
        return (h||g||f);
    }
}