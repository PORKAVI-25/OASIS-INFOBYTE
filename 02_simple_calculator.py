def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    raise ValueError("Unsupported operator.")

def main():
    print("=== Simple Calculator ===")
    try:
        a = float(input("First number: "))
        operator = input("Operator (+, -, *, /): ").strip()
        b = float(input("Second number: "))
        result = calculate(a, operator, b)
        print("Result:", result)
    except ValueError as error:
        print("Input error:", error)
    except ZeroDivisionError as error:
        print("Calculation error:", error)

if __name__ == "__main__":
    main()
