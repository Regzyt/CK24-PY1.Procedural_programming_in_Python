import json
FILENAME = "input.json"
def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    list_values = [item["score"]*item["weight"] for item in json_data]
    return sum(list_values)
if __name__ == '__main__':
    print(f"{task():.3f}")