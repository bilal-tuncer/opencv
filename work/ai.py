import requests
import base64
import json
import os

def req(path,projectName,label,name):
    
    with open(path,"rb") as img_bytes:
        f = img_bytes.read()
        b = bytes(f)

    img_str = base64.urlsafe_b64encode(b).decode("utf-8")
    payload = {
        "ImgStr" : img_str,
        "W" : 128,
        "H" : 128,
        "IsGray" : 0,
        "ProjectName" : projectName,
        "Label" : label,
        "Name" : name
    }
    url = "http://10.148.14.0:9999/preprocess"
    payload = json.dumps(payload)
    headers = {"Content-Type":"application/json"}
    res = requests.request(method="post",url=url,headers=headers,data=payload)
    print(res.content)

if __name__ == "__main__":
    
    path = "/home/bil/Documents/Rakamlar(RGB)/4"
    projectName = "rakamlar4"
    
    for tempdir in os.listdir(path):
        label = "label{}".format(tempdir[2])
        inPath = path + "/"+ tempdir
        j = 1
        for file in os.listdir(inPath):
            name = "tmp{}".format(j)
            file_path = inPath + "/" + file
            req(file_path,projectName,label,name)
            print(label,name,file_path)
            j +=1
