#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print (len(enron_data))
#print (enron_data[1])
#enron_data_lst =  list(enron_data.keys())
enron_data_lst =  list(enron_data.values())
print (len(enron_data_lst[0]))

"""
poi = 0
for i in enron_data:
    for j in enron_data[i]:
        if j=='poi' :
            if enron_data[i][j] == 1:
                poi = poi + 1                
print (poi)
"""

#print (enron_data["PRENTICE JAMES"]["total_stock_value"])
#print (enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print (enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
