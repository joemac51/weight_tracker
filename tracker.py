from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
import json
import os

class tracker:
    '''Weight tracker class'''

    UNITS = 'kg'
    JSON_PATH = "/Users/daniel/Documents/Python/weight_tracker/weight_log.json"

    def __init__(self, kg=True):
        self.kg = kg
        self.weight = 0.0
        self.data = []
        if os.path.exists(self.JSON_PATH) and os.path.getsize(self.JSON_PATH) != 0:
            with open(self.JSON_PATH, 'r') as f:
                self.data = json.load(f)
        else:
            with open(self.JSON_PATH, 'w') as f: # create the json file if it doesn't exist (or is empty)
                json.dump(self.data, f)
        if not kg:
            self.UNITS = 'lbs'

    def log_weight(self, weight):
        self.weight = weight
        # with open(self.JSON_PATH, 'r') as f:
        #     self.data = json.load(f)
        self.data.append({
            "Date": date.today().strftime("%d/%m/%Y"),
            "Weight": self.weight
            })
        with open(self.JSON_PATH, 'w') as f:
            json.dump(self.data, f)

    def plot_weight(self):
        with open(self.JSON_PATH, 'r') as f:
            contents = json.load(f)
            # contents_list = contents.split()
            # # remove units from weights and convert them to numbers
            # contents_list_y = [float(i.rstrip('kg')) for i in contents_list if i.endswith('kg')]
            # # remove semicolon from dates
            # contents_list_x = [i.rstrip(':') for i in contents_list if str(i).endswith(':')]
            x_vals = [contents[i]["Date"] for i in range(len(contents))] # list of dates
            y_vals = [contents[i]["Weight"] for i in range(len(contents))] # list of weights
            sns.lineplot(x_vals, y_vals, markers=True)
            plt.show()

if __name__=="__main__":
    weight_tracker = tracker()
    weight_tracker.log_weight(77.5)
    weight_tracker.plot_weight()
