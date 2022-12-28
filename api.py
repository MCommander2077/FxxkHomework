if __name__ == "__main__":
    import requests
    def Recognize_text(img):
        password='8907'
        url = "http://www.iinside.cn:7001/api_req"
        filePath=img
        text = ""
        data={
            'password':password,
            'reqmode':'ocr_pp'
        }
        files=[('image_ocr_pp',('wx.PNG',open(filePath,'rb'),'application/octet-stream'))]
        headers = {}
        response = requests.post( url, headers=headers, data=data, files=files).text
        for i in eval(response)["data"]:
            text = text + str(i)
        return text

    text = Recognize_text(r"C:\Users\MadYang\PycharmProjects\pythonProject2\搜题\小题题.JPG")
    print(text)