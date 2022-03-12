import json
a={"Name":"Abhishek",
"designation":"CEO of navgurukul",
"Gender":"Male",
"Age":29
}
with open("file7_txt.json","w") as file:
    json.dump(a,file,indent=4)