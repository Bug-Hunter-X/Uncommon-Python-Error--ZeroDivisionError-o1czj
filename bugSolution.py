def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 1
    except ZeroDivisionError:
        return "Division by zero error"

result = function_with_uncommon_error(0)
print(result)  # Output: Division by zero error