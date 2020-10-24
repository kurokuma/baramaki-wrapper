# -*- coding: utf-8 -*-
from baramaki.base import BaramakiAPIBase

class BaramakiTable(BaramakiAPIBase):
    def __init__(self):
        pass

    # def get_tables(self):
    #     return self.get_table(table="tables")
    
    def get_domain(self, date="today", limit=100, offset=0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return self.get_table(table="tables/domain", date=date, params=params)
    
    def get_hash(self, date="today", limit=100, offset=0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return self.get_table(table="tables/hash", date=date, params=params)

    def get_ip(self, date="today", limit=100, offset=0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return self.get_table(table="tables/ipaddress", date=date, params=params)

    def get_url(self, date="today", limit=100, offset=0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return self.get_table(table="tables/url", date=date, params=params)

    def get_task(self, date="today", limit=100, offset=0):
        params = {
            "limit": limit,
            "offset": offset
        }
        return self.get_table(table="tables/task", date=date, params=params)