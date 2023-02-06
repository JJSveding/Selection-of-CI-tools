from dataclasses import dataclass
from typing import Optional


@dataclass
class Filters:
    country_code: Optional[str] = None
    sales_channel: Optional[str] = None
    store_no: Optional[int] = None
    bimonthly_period: Optional[str] = None
