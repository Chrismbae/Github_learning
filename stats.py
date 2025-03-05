def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)

def calculate_variance(data):
    if not data:
        return 0
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)
