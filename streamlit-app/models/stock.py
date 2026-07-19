from dataclasses import dataclass


@dataclass
class Stock:

    symbol:str

    company_name:str

    current_price:float

    sector:str