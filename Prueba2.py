import urllib
import requests
import datetime
main_api = "https://www.mapquestapi.com/directions/v2/route?"
hora_actual = datetime.datetime.now()
print("Hola, Bienvenido ", hora_actual)
while True:
    orig = input("La Ubicacion De Inicio Es: ")
    if orig == "quit" or orig == "h":
        break
    dest = input("El Destino Final Es: ")
    if dest == "quit" or dest == "h":
        break

    key = "wWrRsrjFFkzq0S7ZqlBarOjXNwCC7US1"
    url = main_api + urllib.parse.urlencode ({"key" :key, "from" :orig, "to" :dest})
    json_data = requests.get (url) .json ()
    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
        print ("API Status:” + str (json_status) + “= Una llamada de ruta exitosa.\ n")
       
        print("=============================================")
        print("Origen: " + (orig) + " hasta " + (dest))
        print("Destino: " + (json_data["route"]["formattedTime"]))
        print ("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        #print ("Combustible usado (Gal): "+ str (json_data ["route"] ["FuelUsed"]))#
        #print ("Combustible usado (Ltr): + str "((json_data ["route"] ["FuelUsed"])3.78))#
        print("Hora: ", hora_actual)

    print("=============================================")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")