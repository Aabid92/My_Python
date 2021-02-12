dost = {"Aabid": 23, "Juned": 24, "Usman": 20}    #key is (Aabid)

dost ["Suraj"] = 25

print (dost["Aabid"])

print (dost)

dost1 = [
       
       {"Name": "Aabid","Age": 22, "weith": 66},

       {"Name": "Juned","Age": 23, "weith": 66},

       {"Name": "Aabid","Age": 22, "weith": 66},

       {"Name": "Aabid","Age": 22, "weith": 66},

]   

print (dost1[1]["Name"])
                           
#print (dost1)

student = {"Aabid": 100,  "Juned": 80, "Usman": 55}

for atten , attendance in student.items():
    print(f"{atten}:{attendance}%")

print("\n")
value = {"Juned": 22,"Shaikh": 58,"XYZ": 45}

if "Aabid" in value:
       print(f"Aabid: {value['Aabid']}")
else:
    print("Abid is not in class")
