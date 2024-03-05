# Get expression from user
expr = input("Expression: ").strip()
# Split expression by spaces
spl = expr.split(" ", -1)

# Separate each part of expression into variables
x = spl[0]
operator = spl[1]
y = spl[2]

# Use match for each operator case
match operator:
    case "+":
        print(float(x) + float(y))
    case "-":
        print(float(x) - float(y))
    case "*":
        print(float(x) * float(y))
    case "/":
        print(float(x) / float(y))