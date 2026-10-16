class Solution:
    def isPalindrome(self, s: str) -> bool:
        st="".join(char for char in s if char.isalnum())
        if st.lower() == st[-1::-1].lower():
            return True
        return False