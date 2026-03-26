import re
import json
def pars(path):
    with open(path, "r") as file:
        content=file.read()
    
    prices=re.findall(r"Стоимость\s+(\d+,\d+)", content) #Find a 'Стоимость', skip any spaces, take digits with ','
    product_name=re.findall(r"\d\.\s+(.+)", content) #Find a digit with '.', skip any spaces, and take a text until the end
    total_amount=re.findall(r"ИТОГО:\s+(\d+\s+\d+,\d+)", content) #'()'-grooping
    date_time=re.findall(r"Время:\s+(\d+\.\d+\.\d+\s+\d+\:\d+\:\d+)" ,content)
    canditatesfor_paymentmethod=re.findall(r"([А-яа-я\ ]+)\:\s+\d+\s+\d+\,\d+", content)
    payment_method=canditatesfor_paymentmethod[0]
    result={
        "product name" : product_name,
        "prices" : prices,
        "total amount" : total_amount ,
        "date time" : date_time ,
        "payment method" : payment_method 
    }
    print(json.dumps(result, ensure_ascii=False, indent=4))
pars("raw.txt")