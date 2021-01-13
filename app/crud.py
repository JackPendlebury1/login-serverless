from typing import Optional, Generator, Union, Any, Dict
from fastapi import Depends
import uuid, datetime
from . import models, schemas, security, deps
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from fastapi.encoders import jsonable_encoder


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_password_hash(user.password)
    gID = str(uuid.uuid1())
    gDate = str(datetime.datetime.now())
    db_user = models.User(
        id=gID,
        email=user.email,
        hashed_password=hashed_password,
        first_name = user.first_name,
        last_name = user.last_name,
        gender = user.gender,
        created_at = gDate,
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.UserUpdate, email: str):
    hashed_password = security.get_password_hash(user.password)
    db_user = db.query(models.User).filter(models.User.email == email).update({
    'email' : user.email,
    'hashed_password' : hashed_password,
    'first_name' : user.first_name,
    'last_name' : user.last_name,
    'gender' : user.gender,
    }, synchronize_session='fetch')
    db.commit()
    return db_user

def update_user_image(db: Session, user_id: str , userImage: bytes):
    db_user = db.query(models.User).filter(models.User.id == user_id).update({
        'userImage' : userImage
    })
    db.commit()
    return db_user

##login

def authenticate_user(db: Session, email: str, password: str):
    db_user = get_user_by_email(db, email=email)
    if not db_user:
        return False
    if not security.verify_password(password, db_user.hashed_password):
        return False
    return db_user