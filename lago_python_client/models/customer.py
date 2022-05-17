from pydantic import BaseModel, Field
from typing import Optional


class Customer(BaseModel):
    customer_id: str
    address_line1: Optional[str]
    address_line2: Optional[str]
    city: Optional[str]
    country: Optional[str]
    email: Optional[str]
    legal_name: Optional[str]
    legal_number: Optional[str]
    logo_url: Optional[str]
    name: str
    phone: Optional[str]
    state: Optional[str]
    url: Optional[str]
    vat_rate: Optional[float]
    zipcode: Optional[str]


class CustomerResponse(BaseModel):
    lago_id: str
    customer_id: str
    address_line1: Optional[str]
    address_line2: Optional[str]
    city: Optional[str]
    country: Optional[str]
    email: Optional[str]
    created_at: str
    legal_name: Optional[str]
    legal_number: Optional[str]
    logo_url: Optional[str]
    name: str
    phone: Optional[str]
    state: Optional[str]
    url: Optional[str]
    vat_rate: Optional[float]
    zipcode: Optional[str]