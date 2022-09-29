import pickle,json,numpy as np

class td():
    def __init__(self,age,education,default,balance,housing,loan,day,month,duration,campaign,pdays,previous,job,marital,poutcome):
        self.age=age
        self.education=education
        self.default=default
        self.balance=balance
        self.housing=housing
        self.loan=loan
        self.day=day
        self.month=month
        self.duration=duration
        self.campaign=campaign
        self.pdays=pdays
        self.previous=previous
        self.job=job
        self.marital=marital
        self.poutcome=poutcome

    def model(self):
        with open("knn_model.pickle","rb") as f:
            self.mod=pickle.load(f)

        with open("columns_list.json","r") as f:
            self.cols=json.load(f)

    def output(self):
        self.model()
        arr=np.zeros(len(self.cols["column"]))

        arr[0]=self.age
        arr[1]=self.education
        arr[2]=self.default
        arr[3]=self.balance
        arr[4]=self.housing
        arr[5]=self.loan
        arr[6]=self.day
        arr[7]=self.month
        arr[8]=self.duration
        arr[9]=self.campaign
        arr[10]=self.pdays
        arr[11]=self.previous

        job1="job_"+self.job
        job1_index=self.cols["column"].index(job1)
        arr[job1_index]=1

        marital1="marital_"+self.marital
        marital1_index=self.cols["column"].index(marital1)
        arr[marital1_index]=1

        poutcome1="poutcome_"+self.poutcome
        poutcome1_index=self.cols["column"].index(poutcome1)
        arr[poutcome1_index]=1


        pred=self.mod.predict([arr])

        return pred










