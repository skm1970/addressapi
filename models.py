from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    postal_code: str
    country: str


class AddressCreate(AddressBase):
    name: str


class AddressUpdate(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None


class Address(AddressBase):
    name: str
