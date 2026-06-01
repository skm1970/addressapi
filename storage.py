from typing import Optional
from models import Address, AddressCreate, AddressUpdate

db: dict[str, Address] = {}


def add(data: AddressCreate) -> Address:
    address = Address(**data.model_dump())
    db[address.name] = address
    return address


def get(name: str) -> Optional[Address]:
    return db.get(name)


def get_all() -> list[Address]:
    return list(db.values())


def update(name: str, data: AddressUpdate) -> Optional[Address]:
    address = db.get(name)
    if address is None:
        return None
    updated = address.model_copy(update={k: v for k, v in data.model_dump().items() if v is not None})
    db[name] = updated
    return updated


def delete(name: str) -> bool:
    if name not in db:
        return False
    del db[name]
    return True
