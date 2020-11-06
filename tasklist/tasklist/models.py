# pylint: disable=missing-module-docstring,missing-class-docstring
from typing import Optional

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

# pylint: disable=too-few-public-methods

class UpdateUser(BaseModel):
    old_username: str
    new_username: str

class User(BaseModel):
    username: str

class Task(BaseModel):
    description: Optional[str] = Field(
        'no description',
        title='Task description',
        max_length=1024,
    )
    completed: Optional[bool] = Field(
        False,
        title='Shows whether the task was completed',
    )
    id_owner: int = Field(
        title="Task owner"
    )

    class Config:
        schema_extra = {
            'example': {
                'description': 'Buy baby diapers',
                'completed': False,
                'id_owner': 1
            }
        }
