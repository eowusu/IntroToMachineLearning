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

persons_of_interest = {k : v for k,v in enron_data.items() if v['poi']}

print 'Total People: ', len(enron_data.items())
print len(persons_of_interest), ' persons of interest'
print 'Keys available: ', enron_data["PRENTICE JAMES"].keys()
print 'Total value of stock belonging to James Prentice: ', enron_data["PRENTICE JAMES"]["total_stock_value"]
print 'Total email messages form Wesley Colwell to persons of interests: ', enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print 'Total value of stock options exercised by Jeff Skilling:', enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print ''
print 'Total Payments to Lay:', enron_data["LAY KENNETH L"]["total_payments"]
print 'Total Payments to Skilling', enron_data["SKILLING JEFFREY K"]["total_payments"]
print 'Total Payments to Fastow', enron_data["FASTOW ANDREW S"]["total_payments"]
print 'Quantified Salaries:', len({v["salary"] for k,v in enron_data.items()})
print 'Known Email Addresses:', len({v["email_address"] for k,v in enron_data.items() if v["email_address"] != "NaN"})
print 'Unknown Total Payments', len(enron_data.items()) - len({v["total_payments"] for k,v in enron_data.items()})
print 'Unknown Total Payments to POIs', len(persons_of_interest) - len({v["total_payments"] for k,v in persons_of_interest.items()})
print 'Unknown Total Stock Value of POIs', len(persons_of_interest) - len({v["total_stock_value"] for k,v in persons_of_interest.items()})

