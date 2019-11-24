import requests

if __name__ == "__main__":
    feature1 = str(0.9)
    feature2 = str(0.5)
    feature3 = str(6.0)
    feature4 = str(200.0)
    feature5 = str(6.0)
    feature6 = str(1.0)
    feature7 = str(0.0)
    
    datum_body = {
        "body": [
            {
                "att1": 0.9,
                "att2": 0.5,
                "att3": 6.0,
                "att4": 200.0,
                "att5": 6.0,
                "att6": 1.0,
                "att7": 0.0
            }
        ]
    }

    URL = "http://crowsad.pythonanywhere.com/"
    URL2 = "http://crowsad.pythonanywhere.com/prediction?feature1="+feature1+"&feature2="+feature2+"&feature3="+feature3+"&feature4="+feature4+"&feature5="+feature5+"&feature6="+feature6+"&feature7="+feature7
    #URL = "127.0.0.1"
	
    # sending get request and saving the response as response object 
    #r = requests.get(url = URL, json=datum_body) 
    r = requests.get(url = URL2)
    # extracting data in json format  
    #print(r.json())
    print(URL2)