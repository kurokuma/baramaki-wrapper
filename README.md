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
