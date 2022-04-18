import pickle
import pandas as pd
from generate_features import build_features
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
from elasticsearch import Elasticsearch, helpers
import datetime

# New part
#apply predict to our data
def predict_model(saved_model, df):
        predicted_val = saved_model.predict(df).tolist()
        predicted_confidence_score_val = np.max(saved_model.predict_proba(df), axis=1)

        return predicted_val, predicted_confidence_score_val

        # print("succeeded n2 ")


with open("../models/model_vot.sav", 'rb') as pickle_file:
        saved_model = pickle.load(pickle_file)


df = x_test.copy()

pred_vals, conf_vals = predict_model(saved_model, df)
df["predicted_label"] = pred_vals
df["score"] = conf_vals

df.to_csv("../data/project_test_data_with_prediction.csv", index=False)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)



data = pd.read_csv('../data/project_test_data_with_prediction.csv')

for index, row in data.iterrows():

  df = row.to_dict()
  print(json.dumps(df).encode('utf-8'))


  producer.send("net-bios", value=json.dumps(df).encode('utf-8'))
  producer.flush()

