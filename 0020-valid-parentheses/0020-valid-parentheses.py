class Solution:
    def isValid(self, s: str) -> bool:
        opcl= {'(':')', '[':']', '{':'}'}
        stack= []
        for i in s:
            if i in '({[':
                stack.append(i)
                
            elif len(stack) == 0 or opcl[stack.pop()] != i:
                return False
            
        return len(stack)== 0