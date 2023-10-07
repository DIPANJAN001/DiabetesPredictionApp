import keras
import numpy as np
model=keras.models.load_model("./Model/m1.h5")

def predict_diabetes(glu,bmi,bp,age):
    xs=[[glu,bmi,bp,age]]
    xs=np.array(xs,dtype=np.float32)/300
    ys=model.predict(xs)
    return ys[0][0]

