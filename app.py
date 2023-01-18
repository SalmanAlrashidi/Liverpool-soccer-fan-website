from flask import Flask,render_template,url_for,redirect
import requests
import tweepy
import pandas as pd
from soccer_data_api import SoccerDataAPI
import json

#Tweepy

user_id = '881821981397704704'
def api_connection(): # connect_to_twitter
    bearer_token = ''
    return {'Authorization':'bearer {}'.format(bearer_token)}
headers = api_connection()
def make_request(headers):
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = "query=from:AnythingLFC_"
    return requests.request("GET", url,params=params, headers=headers).json()
response = make_request(headers)
print(response)
def df(response):
    return pd.DataFrame(response['data'])

df = df(response)

app = Flask(__name__)

@app.route('/')



def index():
  soccer_data = SoccerDataAPI()
  data=pd.DataFrame(soccer_data.english_premier())
  header=data.columns.tolist()
  value=data.values.tolist()
  return render_template('homee.html',header=header,value=value)


@app.route('/Lliverpool')
def index1():
  soccer_data = SoccerDataAPI()
  data=pd.DataFrame(soccer_data.english_premier())
  data=data.loc[data['team'] == 'Liverpool']
  tweetts=df
  return render_template('Lliverpool.html',data=data,tweetts=tweetts)

@app.route('/clubs')
def index2():
  soccer_data = SoccerDataAPI()
  data=pd.DataFrame(soccer_data.english_premier())
  return render_template('clubs_new.html')

if __name__ == '__main__':
  app.run(debug=True)



















