# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/


def areBracketsBalanced(expr):
    stack = []

    for bracket in expr:
 
        if bracket in ["[" , "{" , "("]:
            stack.append(bracket)
        elif not stack:
            return False
        else:
            pop_bracket = stack.pop()
            # print(pop_bracket)
            if(pop_bracket=="{" and bracket == "}"):
                # print(pop_bracket)
                pass
            elif (pop_bracket=="[" and bracket == "]"):
                # print(pop_bracket)
                pass
            elif (pop_bracket=="(" and bracket == ")"):
                # print(pop_bracket)
                pass
            else:
                return False
 
    return True

 

# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"
 
    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
 