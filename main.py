# from utils import read_data
# from utils import read_test
# from model import RuleBasedModel
from model import *
from utils import *


def main():
    Accuracy = None

    train_file = 'path/to/train_data.txt'
    test_file = 'path/to/test_data.txt'
    variables = ['ID', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'class']


    print ("========= Reading train dataset =========")
    	# TO DO:
	# use the read data function you created to read the train data
    train = read_data('train_data.txt')
    print(train[0])
    print ("======== Done reading =========.\n")

    print ("========= Reading test data =========")
    	# TO-DO 
	# Read the test  data
    test = read_data('test_data.txt')  
    
    print ("========= Done reading =========.\n")

    print ("==== Training classifier =====")
	# TO-DO
	# Initialize the classifier you built in model.py and return the necessary values
    classf1 = classifier(train)
    print('Train Accuracy = ', classf1.predict())
    print('Class of id is : ', classf1.predict_sample(337))
    print ("======== Done training testclassifier ===========.\n")

    print ("========= Classifying test samples =======")
	# TO-DO 
	# use your classifier to do predictions on all the test samples
    classf1 = classifier(test)
    Accuracy = classf1.predict()
    print('Test Accuracy = ', Accuracy)
    print('Class of id is : ', classf1.predict_sample(3))
    print ("========== Done classifying =======")

    	# TO-DO
	# Evalutate your classifier with the Accuracy function you implemented and return the necessary outputs
    print(f"Model's Accuracy {round(Accuracy*100)} %, model correctly predicted {Accuracy * len(test)} out of {len(test)}")
    print('================================================================')


    print ("finished.\n")

main()
