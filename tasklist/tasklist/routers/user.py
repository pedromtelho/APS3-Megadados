# pylint: disable=missing-module-docstring, missing-function-docstring, invalid-name

from typing import Dict

from fastapi import APIRouter, HTTPException, Depends

from ..database import DBSession, get_db
from ..models import Task, User, UpdateUser

router = APIRouter()

@router.get(
    '',
    summary='List users',
    description='List users'
)
async def get_users(db: DBSession = Depends(get_db)):
    return db.get_users()

@router.post(
    '',
    summary='Creates a new user',
    description='Creates a new user'
)
async def create_user(user: User, db: DBSession = Depends(get_db)):
    try:
        return db.create_user(user.username)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='User already exists',
        ) from exception
    

@router.patch(
    '',
    summary='Edit username',
    description='Edit username',
)
async def alter_task(
        user: UpdateUser,
        db: DBSession = Depends(get_db),
):
    try:
        return db.edit_user(user.old_username, user.new_username)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='User not found',
        ) from exception


@router.delete(
    '/{username}',
    summary='Deletes user',
    description='Deletes user by username',
)
async def remove_user(username: str, db: DBSession = Depends(get_db)):

    try:
        return db.remove_user(username)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='User not found',
        ) from exception


