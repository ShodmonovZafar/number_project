import math
class Number:
    
    def __init__(self, value: int) -> None:
        self.value = value

    def get_number(self) -> int:
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self) -> bool:
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        if self.value % 2 == 0:
            return False
        else:
            return True

    def is_even(self) -> bool:
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        if self.value % 2 == 0:
            return True
        else:
            return False
    
    def is_prime(self) -> bool:
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        if self.value < 2:
            return False
        sqrt_num = math.ceil(math.sqrt(self.value))
        for i in range(2, sqrt_num + 1):
            if self.value % i == 0 and self.value != i:
                return False
        return True
        
    def get_divisors(self) -> list:
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        if self.value < 1:
            return []
        if self.value == 1:
            return [1]
        re_list = [1]
        for i in range(2, self.value + 1):
            if self.value % i == 0:
                re_list.append(i)
        return re_list

    def get_length(self) -> int:
        """
        Returns the number of digits in the number.

        returns: int
        """
        h = len(str(self.value))
        if self.value < 0:
            return h - 1
        return h

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        if self.value < 0:
            s = str(self.value)[1:]
        else:
            s = str(self.value)
        res = 0
        for i in s:
            res += int(i)
        return res

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        if self.value < 0:
            return
        u = self.get_length() - 1
        num = self.value
        ren = 0
        while num > 0:
            ren += (num % 10) * (10 ** u)
            num //= 10
            u -= 1
        return ren

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        if self.value < 0:
            return
        uz = self.get_length()
        if uz % 2 == 0:
            aylanalar_soni = int(uz / 2)
            ch = aylanalar_soni - 1
            ong = aylanalar_soni
        else:
            aylanalar_soni = uz // 2
            ch = aylanalar_soni - 1
            ong = aylanalar_soni + 1
        s = str(self.value)
        for i in range(aylanalar_soni):
            if s[ch] != s[ong]:
                return False
            ch -= 1
            ong += 1
        return True

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        if self.value < 0:
            return
        list_one = []
        num = self.value  # 1423
        while num > 0:
            list_one.append(num % 10)
            num //= 10
        list_one.reverse()
        return list_one

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        if self.value < 0:
            return
        x = self.get_digits()
        if len(x) < 2:
            return self.value
        return max(x)

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        if self.value < 0:
            return
        x = self.get_digits()
        if len(x) < 2:
            return self.value
        return min(x)

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        if self.value < 0:
            return
        return self.get_sum()/self.get_length()
        

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
for i in range(-20, 1000):
    number = Number(i)
    a = number.get_average()
    print("Number: ", i, "Natija: ", a)


