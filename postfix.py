import tokenize


class postfix:
    def __init__(self):
        super().__init__()

    @staticmethod
    def parse_expr(expStr):
        tokens = tokenize.tokenize(expStr)
        OP = ("*", "/", "+", "-", "(", ")")
        P = {
            "*": 50,
            "/": 50,
            "+": 40,
            "-": 40,
            "(": 0
        }
        output = []
        stack = []

        for item in tokens:
            if item not in OP:
                output.append(item)
            elif item == "(":
                stack.append(item)
            elif item == ")":
                while stack != [] and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack != [] and P[stack[-1]] >= P[item]:
                    output.append(stack.pop())
                stack.append(item)

        while stack:
            output.append(stack.pop())

        return output
