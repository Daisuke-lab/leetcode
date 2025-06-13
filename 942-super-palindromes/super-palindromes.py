class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        start_length = len(left)
        end_length = len(right)
        left = int(left)
        right = int(right)
        count = 0
        palindromes = self.generate_palindrome(start_length, end_length)
        for palindrome in palindromes:
            #print(palindrome)
            if palindrome < left:
                continue
            if palindrome > right:
                break
            count += 1
        return count

    def is_square(self, num):
        return int(math.sqrt(num)) ** 2 == num

    def is_palindrome(self, num):
        num = str(num)
        i = 0
        j = len(num) -1
        while i < j:
            if num[i] == num[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def generate_palindrome(self, start_length, end_length):
        if start_length == 1:
            for i in [1, 4, 9]:
                yield i
        # 121=11**2, 484=22**2=11*2**2, 10201=101**2 12321=111**2 14641=121**2=11**2**2, 
        # 40804 = 202**2, 44944=212**2=106*2=4*53

        # try to find 11, 101, 111, 121, 202, 212
        # once it breaks palindrome when you power by 2, you can go to the next length

        # palindrome => square => square palindrome
        # square palindrome => still palindrome
        if start_length <= 3:
            for i in range(1, 10):
                num = int(str(i) + str(i)) ** 2
                if self.is_palindrome(num):
                    yield num
                else:
                    break
        if start_length <= 6:
            for i in range(1, 10):
                for j in range(10):
                    num = int(str(i) + str(j) + str(i)) ** 2
                    if self.is_palindrome(num):
                        yield num
                    else:
                        break
        for length in range(4, 10):
            half = length // 2
            if length % 2 ==0:
                for i in range(10**(half-1), 10**half):
                    num =  int(str(i) + str(i)[::-1]) ** 2
                    # print(num)
                    # print(len(str(num)))
                    if self.is_palindrome(num):
                        yield num
            else:
                for i in range(10**(half-1), 10**half):
                    for j in range(10):
                        num = int(str(i) + str(j) + str(i)[::-1]) **2
                        # print(num)
                        # print(len(str(num)))
                        if self.is_palindrome(num):
                            yield num
                
