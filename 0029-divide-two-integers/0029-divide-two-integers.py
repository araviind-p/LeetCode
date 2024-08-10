class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for the integer limits
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        # Handle special cases
        if divisor == 0:
            raise ValueError("Division by zero is undefined")
        if dividend == 0:
            return 0
        if divisor == 1:
            return min(max(dividend, INT_MIN), INT_MAX)
        if divisor == -1:
            return min(max(-dividend, INT_MIN), INT_MAX)
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Use absolute values for ease of calculation
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Result variable
        quotient = 0
        
        # Perform the division using bitwise shifts
        while dividend >= divisor:
            # Initialize variables for the power of two divisor
            temp_divisor, num_divisors = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1
            
            # Update the dividend and quotient
            dividend -= temp_divisor
            quotient += num_divisors
        
        # Apply the sign to the result
        if negative:
            quotient = -quotient
        
        # Handle overflow cases
        return min(max(quotient, INT_MIN), INT_MAX)
