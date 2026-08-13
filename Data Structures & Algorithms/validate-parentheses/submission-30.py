class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_dict = {')':'(', '}':'{', ']':'['}
        for bracket in s: 
            #since it will check only the keys, we know it is a closing bracket. 
            if bracket in close_open_dict: 
                if stack and stack[-1] == close_open_dict[bracket]: 
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(bracket)

        # if we have not empty stack return False
        return False if stack else True



        