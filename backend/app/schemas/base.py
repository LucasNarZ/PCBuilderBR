from pydantic import BaseModel, ConfigDict
from humps import camelize

class BaseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        from_attributes=True
    )
