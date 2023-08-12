import pickle
import numpy as np

with open(r"static/model_file/knn_classifier.pkl","rb") as f:
    model = pickle.load(f)



def get_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal):
    test_array = np.zeros([1,model.n_features_in_])
    test_array[0,0] = age
    test_array[0,1] = sex
    test_array[0,2] = cp
    test_array[0,3] = trestbps
    test_array[0,4] = chol
    test_array[0,5] = fbs
    test_array[0,6] = restecg
    test_array[0,7] = thalach
    test_array[0,8] = exang
    test_array[0,9] = oldpeak
    test_array[0,10] = slope
    test_array[0,11] = ca
    test_array[0,12] = thal
    predicted_disease = np.around(model.predict(test_array))
    return predicted_disease