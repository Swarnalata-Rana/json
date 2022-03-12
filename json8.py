import json
dict1={"name":"neelam", "Designation":"programmer","age":"34","salary":"24000"}
dict2={"name":"komal","Designation":"Trainee","Age":"24","salary":"20000"}
dict3={"name":"anuradha","Designation":"HR","Age":"25","salary":"40000"}
dict4={ "name":"Abhishek","Designation":"Manager","Age":"29"}
c=[]
c.append(dict1)
c.append(dict2)
c.append(dict3)
c.append(dict4)
with open("file8_txt.json","w") as file:
    json.dump(c,file,indent=4)