from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectId")
        return str(v)

class Task(BaseModel):
    # id: Optional[PyObjectId] = Field(alias="_id")
    id: Optional[str] = Field(alias="_id")
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = { ObjectId: str }

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = { ObjectId: str }


# from pydantic import BaseModel, Field
# from typing import Optional
# from bson import ObjectId


# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectId")
#         return str(v)


# class Task(BaseModel):
#     id: Optional[PyObjectId] = Field(alias="_id", default=None, allow_mutation=False)
#     title: str
#     description: Optional[str] = None
#     completed: bool = False

#     class Config:
#         allow_population_by_field_name = True
#         json_encoders = {ObjectId: str}
#         arbitrary_types_allowed = True
#         orm_mode = True