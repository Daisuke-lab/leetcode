class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(s, p)
        #*を見つける。
        #その一文字前を見る。あんまりよくない。

        #pの一文字目見る。次の文字チェックする。いけるところまで取り除いてrecursion
        if p == ".*":
            return True
        
        elif len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False

        elif len(p) == 1:
            if p == "." and len(s) == 1:
                return True
            elif p == s:
                return True
            else:
                return False
        elif len(s) < 2:
            # len(s) == 1 and p = "."のケースは上で巻き取っている。
            if p == ".*":
                return True
            else:
                return False
        
        regex = p[:2]
        new_p = p[1:]

        #aaとかのケース
        if "." not in regex and "*" not in regex:
            if regex == s[:2]:
                s = s[2:]
                if len(p) >= 3:
                    if p[2] == "*":
                        new_p = p[1:]
                    else:
                        new_p = p[2:]
                else:
                    new_p = p[2:]
                return self.isMatch(s, new_p)
            else:
                return False
        #これも..*の可能性があるから一文字消す
        elif regex == "..":
            s = s[1:]
            return self.isMatch(s, new_p)


        elif regex == ".*":     
            new_p = p[2:]
            j = -1
            result = False
            while j < len(s):
                j += 1
                if self.isMatch(s[j:], new_p):
                    result = True
                    break

            return result

        #a.か.aのケース。
        elif "." in regex and "*" not in regex:
            s = s[1:]
            return self.isMatch(s, new_p)

        #a*のケース
        elif regex[0] not in [".", "*"] and regex[1] == "*":
            new_p = p[2:]
            j = -1
            result = False
            while j < len(s):
                j += 1
                if self.isMatch(s[j:], new_p):
                    result = True
                    break

            return result


        else:
            return self.isMatch(s[1:], new_p)