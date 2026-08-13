class Solution:
    def isValid(self, s: str) -> bool:
    
        """
        The idea is each bracket should be closed. 
        if s = [{({)}]
        we insert = [, 
        since in programing the last opened brakcet should be the one closed. 
        so we use a stack. 
        if it is an opening bracket we insert, if it is a closing bracket, we pop 
        and check does it match the opening one, like ( == ).
        ['(']
        ['{']
        ['(']
        ['{']
        ['[']
        """
        # the opening and closing brakcets have the same order. 
        opening_brackets = ['(', '[', '{']
        closing_brackets = [')', ']', '}']

        if len(s) == 1 or s[0] in closing_brackets:
            return False
        # minimum two for opening and closing brackets
        # or it starts with a closing bracket

        ## Now we can do a simple check that will check if number of opening 
        ## brackets equals closing if not then return False
        num_open = [i for i in s if i in opening_brackets]
        num_close = [j for j in s if j in closing_brackets]

        if len(num_open) != len(num_close): 
            return False
    

        stack = []

        for i in s: 
            if i in opening_brackets: 
                stack.append(i)
            if i in closing_brackets: 
                if len(stack) == 0: 
                    return False
                pop = stack[-1]
                stack[:] = stack[:-1]
                if closing_brackets.index(i) != opening_brackets.index(pop): 
                    return False
        return True

        