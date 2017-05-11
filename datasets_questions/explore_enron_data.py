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
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

'''
  Total numbers
'''
total_numbers = len(enron_data)
# print total_numbers

'''
  Find out the intersts numbers
'''
interests = 0

for key in enron_data:
  if enron_data[key]['poi'] == 1:
    interests = interests + 1

# print(interests)

'''
  Find out the max total_payments
'''
# for key in enron_data:
#   if "SKILLING JEFFREY K" in key:
#     print key, enron_data[key]
#   if "LAY KENNETH L" in key:
#     print key, enron_data[key]
#   if "FASTOW ANDREW S" in key:
#     print key, enron_data[key]

'''
  Find out quantified salary people
  # result: 95
'''
# quantified_salary_number = 0

# for key in enron_data:
#   if enron_data[key]['salary'] != 'NaN':
#     quantified_salary_number = quantified_salary_number + 1

# print quantified_salary_number

'''
  Find out quantified salary people
  # result: 111
'''
# notnull_email_number = 0

# for key in enron_data:
#   if enron_data[key]['email_address'] != 'NaN':
#     notnull_email_number = notnull_email_number + 1

# print notnull_email_number

nan_total_payment_number = 0

for key in enron_data:
  if enron_data[key]['total_payments'] == 'NaN':
    nan_total_payment_number = nan_total_payment_number + 1

print nan_total_payment_number

'''
  Find out nan total_payments numbers
'''
# nan_total_payment_poi_number = 0

# for key in enron_data:
#   if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == 1:
#     nan_total_payment_poi_number = nan_total_payment_poi_number + 1

# print nan_total_payment_poi_number

# poi_percent = nan_total_payment_poi_number * 1. / interests
# print poi_percent



