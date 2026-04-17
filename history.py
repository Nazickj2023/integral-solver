import json

class History:
    def __init__(self, history_file='history.json'):
        self.history_file = history_file
        self.load_history()

    def load_history(self):
        try:
            with open(self.history_file, 'r') as f:
                self.history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.history = []

    def add_entry(self, integral, result):
        self.history.append({'integral': integral, 'result': result})
        self.save_history()

    def save_history(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=4)

    def show_history(self):
        return self.history

# Example usage
if __name__ == '__main__':
    history = History()
    history.add_entry('x^2', '1/3*x^3 + C')
    print(history.show_history())