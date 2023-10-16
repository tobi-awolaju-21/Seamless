from typing import Union
#import nessary libary so you can red from firebase both to check if the  instance is enabled
#import square api if there is any 


from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

    #accept the incoming paramena that the api is expecting : msg
    #and the second paramenter the api is expecting instace firebase path :path

    # set the varable value for alll the nedded key eg google ai api key and squaree api key

     #check if the instance is enabled by vhecking the firebase path  : path/settings and check for key enabled, if value is true then

     #get  transformer1 txt from firebase rdb path seamless/transformer1

      #get  transformer2 txt from firebase rdb path seamless/transformer2


     #prompt = transformer + category + transformer 2 + msg
     

     #send the prompt to google palm 2 ai api 
    
     #return the response as the api response.
     #make a call to the marking api when ever ther is an
