import json
import pickle
import numpy as np

__location=None
__column=None
__model=None

def get_price(location,sqft,bhk,bath):
    try:
        loc_index =__column.index(location.lower())
    except:
        loc_index=-1

    x = np.zeros(len(__column))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >=0:
        x[loc_index]=1
    
    return round(__model.predict([x])[0],2)

def get_location_name():
    return __location

def load_data():
    global __column
    global __location
    

    with open("columns.json",'r') as f:
        __column = json.load(f)['column']
        __location=__column[3:]
    global __model
    with open('house_price.pkl','rb') as f:
        __model=pickle.load(f)

if __name__=='__main__':
    load_data()
    print(get_location_name())
    print(get_price('Uttarahalli',1440.0, 2, 3))
