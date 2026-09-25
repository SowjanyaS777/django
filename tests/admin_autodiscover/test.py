def calculate(left, operator, right):
	"""Calculate a result using a basic arithmetic operator."""
	if operator == "+":
		return left + right
	if operator == "-":
		return left - right
	if operator == "*":
		return left * right
	if operator == "/":
		if right == 0:
			raise ZeroDivisionError("cannot divide by zero")
		return left / right
	raise ValueError(f"unsupported operator: {operator}")
