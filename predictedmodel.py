from fastai.vision.all import *


def predict_class(image_path):
    print(image_path)
   
    loaded_model = load_learner("./model/trainedmodel.pkl")

   
    prediction, _, _ = loaded_model.predict(image_path)

    return prediction



