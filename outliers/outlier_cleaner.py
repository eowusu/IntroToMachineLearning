#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    from sklearn import linear_model

    reg = linear_model.LinearRegression()
    reg.fit(ages, net_worths)

    tupled_data = map(lambda x, y, z: (x[0], y[0], abs(y[0] - z[0])), ages, net_worths, predictions)
    tupled_data.sort(key= lambda tup: abs(tup[2]))

    for tup in tupled_data:
        print tup


    cleaned_data = tupled_data[:81]

    ### your code goes here

    
    return cleaned_data

