from pydantic import BaseModel
from typing import List
from .category import CategoryResponse
from .wardrobe import WardrobeResponse
from .photo import PhotoCreate, PhotoResponse


class ItemBase(BaseModel):
    name: str
    price: int
    is_price_fixed: bool
    is_for_rent: bool


class ItemResponse(ItemBase):
    item_id: int
    category: CategoryResponse
    wardrobe: WardrobeResponse
    photos: List[PhotoResponse] = []

    class Config:
        orm_mode = True


class ItemCreate(BaseModel):
    name: str
    price: int
    is_price_fixed: bool
    is_for_rent: bool
    category: int
    wardrobe: int
    photos: List[PhotoCreate]


class ItemUpdate(BaseModel):
    name: str | None = None
    price: int | None = None
    is_price_fixed: bool | None = None
    is_for_rent: bool | None = None
    category_id: int | None = None
    wardrobe_id: int | None = None
    photo_ids: List[int] | None = None
