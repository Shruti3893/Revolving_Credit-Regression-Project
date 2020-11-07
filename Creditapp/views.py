from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
import pandas as pd
from pandas import DataFrame
import numpy as np
import pickle

reg_dt=pickle.load(open("DT_model.pkl", "rb"))

def home(request):
    return render(request, "home.html")

def RevolvingCredit(request):
    try:
        if request.method == 'POST':
            try:
                df = pd.read_csv(request.FILES['files'])
            except:
                df = pd.read_excel(request.FILES['files'], sheet_name=1)
            X = df[['loan_amnt ','Rate_of_intrst','annual_inc','debt_income_ratio','numb_credit','total_credits','total_rec_int','tot_curr_bal']]
            X.columns = X.columns.str.rstrip()
            X.columns = X.columns.str.lstrip()
            X.fillna(X.mean(),inplace=True)
            for col in X.columns:
                percentiles = X[col].quantile([0.10,0.90]).values
                X[col][X[col]<=percentiles[0]]= percentiles[0]
                X[col][X[col]>=percentiles[1]]= percentiles[1]
            pred_value = np.array(reg_dt.predict(X))
            Loan_val = np.array(X['loan_amnt'])
            final_prediction = pd.Series(pred_value, index = Loan_val)
            pred_dict = final_prediction.to_dict()
            context = {"pred_dict" : pred_dict}
            return render(request, "result.html", context = context)
        else:
            return render(request, "home.html")
    except:
        return HttpResponse("Sorry!!! We are unable to process. Your file has some Incorect Information. Please Check and try again...Thank You!!!")

   
def RevolvingCreditValue(request):
    try:
        if request.method == 'POST':
            loan_amnt = float(request.POST['loan_amnt ']) 
            Rate_of_intrst=float(request.POST['Rate_of_intrst'])
            annual_inc=float(request.POST['annual_inc'])
            debt_income_ratio=float(request.POST['debt_income_ratio'])
            numb_credit=float(request.POST['numb_credit'])
            total_credits=float(request.POST['total_credits'])
            total_rec_int=float(request.POST['total_rec_int'])
            tot_curr_bal=float(request.POST['tot_curr_bal'])
            features_list=[loan_amnt ,Rate_of_intrst,annual_inc,debt_income_ratio,numb_credit,total_credits,total_rec_int,tot_curr_bal]
            #features = pd.DataFrame(np.array(features_list),columns=['loan_amnt','Rate_of_intrst','annual_inc','debt_income_ratio','numb_credit','total_credits','total_rec_int','tot_curr_bal'])
            features=np.array(features_list).reshape(-1,8)
            prediction_text = reg_dt.predict(features)
            #import numpy as np    
            #df = pd.DataFrame(np.array(your_data), columns=columns)
            #features_list=[val for val in request.get.values().astype(float)]
            #features = DataFrame (feature_List,columns=['loan_amnt','Rate_of_intrst','annual_inc','debt_income_ratio','numb_credit','total_credits','total_rec_int','tot_curr_bal'])
            #features=features.reshape(-1, 1)
            #features = pd.DataFrame(features)
            # names = regressor.get_booster().feature_names
            #prediction_text = regressor.predict(features)
            #f_names = regressor.feature_names
            #features = features[f_names]
            ########prediction_text= reg_dt.predict(features)
            #cols_when_model_builds = regressor.get_booster().feature_names
            #prediction_text = prediction_text[cols_when_model_builds]
            #prediction_text = reg_dt.predict(features)
            #context = {"prediction_text" : prediction_text}
            return render(request, 'home.html', {"prediction_text" : prediction_text})
        else:
            return render(request, 'home.html')

    except ValueError as e: 
        return HttpResponse(e.args[0], status.HTTP_400_BAD_REQUEST) 
