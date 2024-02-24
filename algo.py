def split_func(text):
    operators = set("+-*/%")
    result = []
    current_token = ""

    for char in text:
        if char in operators or char in "()":
            if current_token:
                result.append(current_token)
                current_token = ""
            if char != " ":
                result.append(char)
        else:
            current_token += char

    if current_token:
        result.append(current_token)

    return result


def calculator(tokens):
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2}

    def apply_operator(operand1, operand2, operator):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
        elif operator == "%":
            return operand1 % operand2
        else:
            raise ValueError("Invalid operator: {}".format(operator))

    def shunting_yard(tokens):
        output = []
        operator_stack = []

        for token in tokens:
            if token.replace(".", "", 1).isdigit():
                output.append(float(token))
            elif token in operators:
                while (
                    operator_stack
                    and operator_stack[-1] in operators
                    and operators[token] <= operators[operator_stack[-1]]
                ):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == "(":
                    operator_stack.pop()
                else:
                    raise ValueError("Mismatched parentheses")

        while operator_stack:
            if operator_stack[-1] == "(":
                raise ValueError("Mismatched parentheses")
            output.append(operator_stack.pop())

        return output

    def evaluate_rpn(rpn_tokens):
        operand_stack = []

        for token in rpn_tokens:
            if isinstance(token, float):
                operand_stack.append(token)
            elif token in operators:
                if len(operand_stack) < 2:
                    raise ValueError(
                        "Invalid expression: Not enough operands for operator '{}'".format(
                            token
                        )
                    )
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = apply_operator(operand1, operand2, token)
                operand_stack.append(result)

        if len(operand_stack) != 1:
            raise ValueError(
                "Invalid expression: The expression was not fully evaluated"
            )

        return operand_stack[0]

    try:
        rpn_tokens = shunting_yard(tokens)
        result = evaluate_rpn(rpn_tokens)
        return result
    except Exception as e:
        raise ValueError("Invalid expression: {}".format(e))


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0
    computeLPSArray(pat, M, lps)
    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            global index_of_optr
            index_of_optr = i - j
            j = lps[j - 1]
            return index_of_optr
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    len = 0
    lps[0]
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def changeValue(result):
    result = str(result)
    if KMPSearch(".", result):
        for i in result[index_of_optr:]:
            if i == "0":
                result = str(int(float(result)))
        return result
    else:
        return result


def result_func(js_string):
    txt = js_string
    result = split_func(txt)
    try:
        result = calculator(result)
        result = round(result, 7)
        Result = changeValue(result)
        return Result
    except ValueError as e:
        return e
