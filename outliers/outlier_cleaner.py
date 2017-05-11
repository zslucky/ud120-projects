#!/usr/bin/python
import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = net_worths

    ### your code goes here
    dataset_length = predictions.shape[0]
    removed_length = dataset_length * 0.1

    distance_arr = numpy.fabs(cleaned_data - predictions)
    index = numpy.argmax(distance_arr)

    while removed_length > 0:
        removed_length = removed_length - 1

        distance_arr = numpy.delete(distance_arr, index)
        cleaned_data = numpy.delete(cleaned_data, index)
        ages = numpy.delete(ages, index)

        index = numpy.argmax(distance_arr)

    return ages, cleaned_data, []


'''
    test data
'''
# ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# net_worths = [10, 20, 30, 45, 52, 61, 72, 81, 99, 101, 112]

# prediction = [10, 25.2, 27.1, 45.1, 58, 59, 72, 83, 91, 111, 118]

# ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
# net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
# prediction = numpy.reshape( numpy.array(prediction), (len(prediction), 1))

# clean_data = outlierCleaner(prediction, ages, net_worths)

# print(clean_data)