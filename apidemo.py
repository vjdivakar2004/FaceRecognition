import requests

url="http://localhost/project/savestudent.php" #url of the server to which we need to send a request

def save_to_db(name):
    param={
        "name":name
    }#we want name to be generic not static so create dictionary 
    resp=requests.get( url,params=param)#sends request to localhost server

    print(resp)#print 200 if  successfull
    
    print(resp.text)#print in console the echo sts of  php file (basically we want to show response sent by server in console)
