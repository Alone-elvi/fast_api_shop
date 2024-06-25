from sqlalchemy.orm import Session
from models.user import User, USER_TYPES
from schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def create_user(db: Session, user: UserCreate):

    if user.user_type not in USER_TYPES:
        raise ValueError(f"Invalid user type: {user.user_type}")

    db_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
        user_type=user.user_type,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise ValueError("User not found")

    if user_update.username:
        db_user.username = user_update.username
    if user_update.email:
        db_user.email = user_update.email
    if user_update.password:
        db_user.password = get_password_hash(user_update.password)
    if user_update.user_type:
        if user_update.user_type not in USER_TYPES:
            raise ValueError(f"Invalid user type: {user_update.user_type}")
        db_user.user_type = user_update.user_type
    if user_update.status:
        db_user.status = user_update.status

    db.commit()
    db.refresh(db_user)
    return db_user
