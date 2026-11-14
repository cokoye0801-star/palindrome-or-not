def check_palindrome():
    print("--- Palindrome Number Checker ---")
    
    try:
        # Input a number from the user
        num = int(input("Enter an integer: "))
        
        # Negative numbers are generally not considered palindromes due to the minus sign
        if num < 0:
            print("❌ Negative numbers are not considered palindromic.")
            return
            
        original_num = num
        reversed_num = 0
        
        # Reverse the number mathematically
        while num > 0:
            digit = num % 10
            reversed_num = (reversed_num * 10) + digit
            num = num // 10
            
        # Check if the original number matches the reversed number
        if original_num == reversed_num:
            print(f"✅ Yes! {original_num} is a PALINDROME number.")
        else:
            print(f"❌ No, {original_num} is NOT a palindrome. (Reversed: {reversed_num})")
            
    except ValueError:
        print("❌ Please enter a valid integer.")

# Run the function
if __name__ == "__main__":
    check_palindrome()
