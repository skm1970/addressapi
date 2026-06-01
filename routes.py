from fastapi import APIRouter, HTTPException
from models import Address, AddressCreate, AddressUpdate
import storage

router = APIRouter(prefix="/addresses", tags=["addresses"])


@router.post("/", response_model=Address, status_code=201)
def create_address(data: AddressCreate):
    if storage.get(data.name):
        raise HTTPException(status_code=409, detail=f"Address '{data.name}' already exists")
    return storage.add(data)


@router.get("/", response_model=list[Address])
def list_addresses():
    return storage.get_all()


@router.get("/{name}", response_model=Address)
def get_address(name: str):
    address = storage.get(name)
    if address is None:
        raise HTTPException(status_code=404, detail=f"Address '{name}' not found")
    return address


@router.put("/{name}", response_model=Address)
def update_address(name: str, data: AddressUpdate):
    address = storage.update(name, data)
    if address is None:
        raise HTTPException(status_code=404, detail=f"Address '{name}' not found")
    return address


@router.delete("/{name}", status_code=204)
def delete_address(name: str):
    if not storage.delete(name):
        raise HTTPException(status_code=404, detail=f"Address '{name}' not found")
