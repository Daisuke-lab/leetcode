class Solution:
    # available value in the first digit: 1 ~ 3, 1 ~ 13
    # after the character you can do anything, but make sure if it's in range
    # let's say first digit is k. It has to be length + k -1 < 9, otherwise number will be overflow

    # Btw, it returns the list and still uses DP
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        str_low = str(low)
        str_high = str(high)
        first_digit = str_low[0]
        last_digit = str_high[:len(str_high) - len(str_low)+1]
        digit_num = len(last_digit) - len(first_digit) + 1
        first_digit = int(first_digit)
        last_digit = int(last_digit)
        start_digits = []
        stop_sign = False
        for i in range(1, digit_num+1):
            for j in range(1, 10):
                # 1,2,3,4,5,6,7,8,9
                # 12, 23, 34, 45, 67
                if j + i -1 >= 10:
                    continue
                start_digit = int("".join([str(j + k) for k in range(i)]))
                if start_digit > last_digit:
                    stop_sign = True
                    break
                if first_digit <= start_digit and start_digit <= last_digit:
                    start_digits.append(start_digit)
            if stop_sign:
                break

        #print(start_digit)
        length =  len(str_low)-1  # len(str_high) - (len(str_high) - len(str_low)+1)
        answers = []
        for start_digit in start_digits:
            start_num = int(str(start_digit)[-1])
            if length + start_num <= 9:
               answer = str(start_digit) + "".join([str(i + start_num) for i in range(1, length+1)])
               answer = int(answer)
               #print(answer)
               if low <= answer and answer <= high:
                answers.append(answer)
        return answers 

        