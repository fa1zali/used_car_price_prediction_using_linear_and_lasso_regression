from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import pickle
import json
import numpy as np

app = FastAPI()

loaded_ls_model = pickle.load(open('saved_model/car_price_ls_model.sav', 'rb'))

class Fuel(str, Enum):

    petrol = "Petrol"
    diesel = "Diesel"
    cng = "CNG"

fuel_dct = {"Petrol":2, "Diesel":1, "CNG":0}

class Seller(str, Enum):

    dealer = "Dealer"
    individual = "Individual"

seller_dct = {"Individual":1, "Dealer":0}

class Transmission(str, Enum):

    manual = "Manual"
    automatic = "Automatic"

transmission_dct = {"Manual":1, "Automatic":0}

class Owner(int, Enum):
    zero = 0
    one = 1
    three = 3

class Car(BaseModel):

    Year : int
    Present_Price : float
    Kms_Driven : int
    Fuel_Type : Fuel
    Seller_Type : Seller
    Transmission : Transmission
    Owner : Owner

@app.post("/get_car_price")
def get_car_price(input_parameters:Car):
    input_data = input_parameters.json()
    input_dct = json.loads(input_data)

    a = input_dct["Year"]
    b = input_dct["Present_Price"]
    c = input_dct["Kms_Driven"]
    d = input_dct["Fuel_Type"]
    e = input_dct["Seller_Type"]
    f = input_dct["Transmission"]
    g = input_dct["Owner"]

    d = fuel_dct.get(d)
    e = seller_dct.get(e)
    f = transmission_dct.get(f)

    input_list = [a,b,c,d,e,f,g]
    input_data_arr = np.asarray(input_list)
    input_data_reshaped = input_data_arr.reshape(1, -1)

    price = loaded_ls_model.predict(input_data_reshaped)
    
    return {'price':price[0]}