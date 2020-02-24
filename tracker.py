from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt

class tracker:
    
    UNITS = 'kg'

    def __init__(self, kg=True):
        self.kg = kg
        self.weight = 0.0

        if not kg:
            self.UNITS = 'lbs'

    def log_weight(self, weight):
        self.weight = weight
        with open("/Users/daniel/Documents/Python/weight_tracker/weight_log.txt", 'a') as f:
            f.write(f'{date.today()}: {self.weight}{self.UNITS}\n')

    def plot_weight(self):
        with open("/Users/daniel/Documents/Python/weight_tracker/weight_log.txt", 'r') as f:
            contents = f.read()
            contents_list = contents.split()
            # remove units from weights and convert them to numbers
            contents_list_y = [float(i.rstrip('kg')) for i in contents_list if i.endswith('kg')]
            # remove semicolon from dates
            contents_list_x = [i.rstrip(':') for i in contents_list if str(i).endswith(':')]
            sns.lineplot(contents_list_x, contents_list_y, markers=True)
            plt.show()

if __name__=="__main__":
    weight_tracker = tracker()
    weight_tracker.log_weight(77.5)
    weight_tracker.plot_weight()
