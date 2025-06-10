def main():
    day = "Monday"

    match day:
        case "Monday":
            print("Start of work week")
        case "Friday":
            print("End of work week")
        case _:
            print("Midweek day")

main()

def main():
    status_code = 404

    match status_code:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Server Error")
        case _:
            print("Unknown Status")

main()

def http_error(status):
    match status:
        case 400 | 401 | 403:
            print("Client error")
        case 404:
            print("Not found")
        case 500 | 502 | 503:
            print("Server error")
        case _:
            print("Unknown")

http_error(403)

def process(value):
    match value:
        case [x, y]:
            print(f"List of 2 items: {x}, {y}")
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case _:
            print("Something else")

process({"name": "Alice", "age": 30})
