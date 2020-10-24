# ninoseki
baramaki-wrapper

- sample

```python
from baramaki.baramaki_table import BaramakiTable
from datetime import datetime

def main():
    b = BaramakiTable()
    
    # domain 
    # today
    print(b.get_domain())
    
    # hash
    # set datetime
    print(b.get_hash(date=datetime(2020, 10, 25)))
    
    # ipaddress
    # limit 10
    # offset 5
    print(b.get_ip(limit=10, offset=5))
    
    # url
    print(b.get_url())
    
    # task
    print(b.get_task())


if __name__ == "__main__":
    main()
```

| param  | Required/Option | Default | Type     | 
| ------ | --------------- | ------- | -------- | 
| date   | Option          | "today" | datetime | 
| limit  | Option          | 100     | int      | 
| offset | Option          | 0       | int      | 

- Return sample

```
[{'artifact': 'http://bjshengquan.com/', 'referenceLink': 'https://twitter.com/KesaGataMe0/status/1319996497216192512', 'referenceText': 'SMBC/三井住友カードのフィッシングサイト情報です。\nフィッシングメールにご注意ください。\n\nhxxp://bjshengquan.com/\n-&gt;192.3.81.11\n(AS36352 / AS-COLOCROSSING, )\n\nhttps://urlscan.io/result/6ee3a5ae-e7e7-4fc4-877e-45a0afb3cdaf/\n\n#Phishing #SMBC #SMCC #三井住友カード https://t.co/HizcFU6jeJ', 'createdDate': '2020-10-24 13:45:59', 'state': None}, {'artifact': 'http://techpastry.com/', 'referenceLink': 'https://twitter.com/KesaGataMe0/status/1319997356578795525', 'referenceText': 'SMBC/三井住友カードのフィッシングサイト情報です。\nフィッシング 
メールにご注意ください。\n\nhxxp://techpastry.com/\n-&gt;192.3.81.11\n(AS36352 / AS-COLOCROSSING, )\n\nhttps://urlscan.io/result/a1b6f70d-8558-415c-bb54-5510e6a9cc1e/\n\n#Phishing #SMBC #SMCC #三井住友カード https://t.co/4id3zjHqnq', 'createdDate': '2020-10-24 13:45:59', 'state': None}, {'artifact': 'https://my.jcb.co.jp-909873.biz/jp/login.php/...', 'referenceLink': 'https://twitter.com/KesaGataMe0/status/1319992701761196032', 'referenceText': 'JCBのフィ 
ッシングサイト情報です。\n#フィッシングメール にご注意ください。\n\nhxxps://my.jcb.co.jp-909873.biz/jp/login.php/...\n-&gt;128.199.89[.]15 \n(AS 14061 / DigitalOcean, LLC )\n\n#Phishing #MyJCB #JCB https://t.co/UJ1rWDcAKE', 'createdDate': '2020-10-24 13:30:59', 'state': None}, {'artifact': 'http://smbc-card.co.jp-909873.club/smbc/..', 'referenceLink': 'https://twitter.com/KesaGataMe0/status/1319993785372139521', 'referenceText': 'SMBC/三井住友カードのフィ 
ッシングサイト情報です。\nフィッシングメールにご注意ください。\n\nhxxp://smbc-card.co.jp-909873.club/smbc/..\n-&gt;128.199.89.15\n(AS 14061 / DigitalOcean, LLC )\n\nhttps://urlscan.io/result/8678922c-53af-4a98-b6c9-42f36fffdf9e/\n\n#Phishing #SMBC #SMCC #三井住友カード https://t.co/X4AOpWh077', 'createdDate': '2020-10-24 13:30:59', 'state': None}, {'artifact': 'https://smbc.co.jp-asitjbe28u3m2g31i5fe.jden.cn/', 'referenceLink': 'https://twitter.com/harugasumi/status/1319975965791981568', 'referenceText': '「＜重要＞【三井住友カード】ご利用確認のお願い」の件名で、三井住友カードを騙るフィッシングメール。\n誘導先URLが長くて省略しますが、\nhxxps://smbc[.]co.jp-ASitJbe28u3m2G31I5Fe.jden[.]cn/\nのホストにて、フィッシングサイト営業中ですので、騙されないよう、お気を付け下さい。 https://t.co/VRVRpOClY5', 'createdDate': '2020-10-24 12:30:57', 'state': None}]
```
