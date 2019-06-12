import requests
import datetime as dt
import time

urlExt = 'https://mindicador.cl/api/dolar/'
urlMyApi = 'http://18.231.117.65:8000/back/usd_prices/'
hdrs={"Content-Type": "application/json"}
Emsg=""
iniDate = dt.date(2018, 1, 1)
today = dt.date.today()

while (iniDate <= today):
    dateA = iniDate.strftime("%d-%m-%Y")
    newUrl = urlExt + dateA
    print(newUrl)

    try :
        resA = requests.get(newUrl)
        
        if resA.status_code == 200 :
#            if resA.json()['serie'] != [] :
            try:
                value = resA.json()['serie'][0]['valor']
            except:
                iniDate = iniDate + dt.timedelta(days=1)
                print("Sin datos")
                time.sleep(3)
                pass
            dateB = iniDate.strftime("%Y-%m-%d")
            data = '{"clp_value": '+ value +', "date": '+ date +' }'
            try:
                resB = requests.post(urlMyApi, headers = hdrs, data = data)
                if resB.status_code != 201 :
                    print("Error -B- al insertar")
                    print("status_code " + resB.status_code)
                    break
            except:
                print("Error -A- al insertar")

                break
        else:
            print("Error -B- al consultar")
            break
    except:
        print( "Error -A- al consultar")
        break

    iniDate = iniDate + dt.timedelta(days=1)
    time.sleep(3)

print(iniDate.strftime("%Y-%m-%d"))

#print(res.status_code)

#print(res.text)

#print(res.json()['serie'][0]['fecha'][:10])
#print(res.json()['serie'][0]['valor'])
