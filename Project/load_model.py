import pickle
import pandas as pd
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
# 'Income', 'House_age', 'Number_of_rooms', 'Number_of_bedrooms', 'Population'
def model_operation(income, house_age,number_of_rooms, number_of_bedrooms,population):
    income=float(income)
    house_age=float(house_age)
    number_of_rooms=float(number_of_rooms)
    number_of_bedrooms=float(number_of_bedrooms)
    population=float(population)
    predict_data={"income":income,
                     "House_age":house_age,
                     "Number_of_rooms":number_of_rooms,
                     'Number_of_bedrooms':number_of_bedrooms,
                     "Polulation":population}
    predict_data=pd.DataFrame(predict_data,index=[0])
    result=loaded_model.predict(predict_data)
    return result