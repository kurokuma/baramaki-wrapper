# ninoseki
baramaki-wrapper

- sample

```python
from baramaki.baramaki_table import BaramakiTable

def main():
    b = BaramakiTable()
    
    # domain
    print(b.get_domain())
    
    # hash
    print(b.get_hash())
    
    # ipaddress
    print(b.get_ip())
    
    # url
    print(b.get_url())
    
    # task
    print(b.get_task())


if __name__ == "__main__":
    main()
```
