import csv
import random
import utils

# load dataset and randomly split it into test set and training set



class classifier:
    def __init__(self, data_set):
        self.data_set = data_set
        self.output = []
        self.count = 0

    def predict(self):
        for i in self.data_set:
            if i['f1'] + i['f2']+ i['f5'] < 1.11:
                self.output.append(2)
                if i['class'] == 2:
                    self.count += 1
            else:
                self.output.append(1)
                if i['class'] == 1:
                    self.count += 1

        return self.count / len(self.data_set) 

    def predict_sample(self, ID):
        # data: list of dicts
        for i in self.data_set:
            if i['ID'] == ID:
                if i['f1'] + i['f2']+ i['f5'] < 1.11:
                    return 2
                else:
                    return 1

          





        

                


        






#print(train)

