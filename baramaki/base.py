# -*- coding: utf-8 -*-
import json
import requests
from datetime import datetime

class BaramakiException(Exception):
    def __init__(self, status_code, url, params):
        self.status_code = status_code
        self.url = url
        self.params = params
    
    def __repr__(self):
        return "Error -> status_code={status_code}, url: {url}, params: {params}".format(
            status_code=self.status_code,
            url=self.url,
            params=self.params
        )

    __str__ = __repr__

class BaramakiInvalidParameterException(BaramakiException):
    pass

class BaramakiAPIBase(object):
    BASE_URL = "http://baramaki.ninoseki.xyz:8000/api/{path}"
    BASE_HEADER = {
        "User-Agent": "Python API",
    }
    EXCEPTION = {
        400: BaramakiInvalidParameterException
    }
    
    def __init__(self):
        pass
    
    def get_query(self, table, params):
        r = requests.get(
            url=self.BASE_URL.format(path=table),
            params=params,
            headers=self.BASE_HEADER,
        )
        r.encoding = r.apparent_encoding
        if r.status_code == 200:
            return r.json()
        else:
            ex = self.EXCEPTION.get(r.status_code, BaramakiException)
            raise ex(
                status_code=r.status_code,
                url=self.BASE_URL.format(path=table),
                params=params
            )
    
    def get_table(self, table, date, params):
        if date == "today":
            date = datetime.now().date()

        if (type(datetime.now()) != type(date)):
            print("date is 'today' or 'datetime.date' class")
            exit(1)

        res = self.get_query(table, params=params)
        output = []
        for row in res:
            created_date = datetime.strptime(row["createdDate"], "%Y-%m-%d %H:%M:%S").date()
            if created_date == date:
                output.append(row)
        return output
