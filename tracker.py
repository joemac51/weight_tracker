from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
import json
import os

class tracker:
    '''A class for tracking body weight'''

    UNITS = 'kg'
    JSON_PATH = "/Users/daniel/Documents/Python/weight_tracker/weight_log.json"

    def __init__(self, kg=True):
        self.kg = kg
        self.weight = 0.0
        self.data = []
        if os.path.exists(self.JSON_PATH) and os.path.getsize(self.JSON_PATH) != 0:
            with open(self.JSON_PATH, 'r') as f:
                self.data = json.load(f) # List of dictionaries containing dates and corresponding weights
        else:
            with open(self.JSON_PATH, 'w') as f: # create the json file if it doesn't exist (or is empty)
                json.dump(self.data, f)
        if not kg:
            self.UNITS = 'lbs'

    def set_weight(self):
        while True:
            try:
                self.weight = float(input("Enter Weight: "))
                break
            except:
                print("Please enter a valid number!")
        return self.weight
    
    def log_weight(self):
        if self.data[len(self.data)-1]["Date"] == date.today().strftime("%d/%m/%Y"):
            self.data[len(self.data)-1]["Weight"] = self.set_weight()
        else:
            self.data.append({
                "Date": date.today().strftime("%d/%m/%Y"),
                "Weight": self.set_weight()
                })
        with open(self.JSON_PATH, 'w') as f:
            json.dump(self.data, f)

    def plot_weight(self):
        with open(self.JSON_PATH, 'r') as f:
            contents = json.load(f)
            x_vals = [contents[i]["Date"] for i in range(len(contents))] # list of dates
            y_vals = [contents[i]["Weight"] for i in range(len(contents))] # list of weights
            sns.lineplot(x_vals, y_vals, color='red', marker='o', mec='black', mfc='black')
            plt.show()

if __name__=="__main__":
    weight_tracker = tracker()
    weight_tracker.log_weight()
    weight_tracker.plot_weight()
