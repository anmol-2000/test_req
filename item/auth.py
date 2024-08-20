from datetime import datetime, timedelta
from fastapi import HTTPException, Request
from passlib.context import CryptContext
from jose import JWTError, jwt

secret_key = 'jdhjgdyudajddje'
algorithm = 'HS256' 

#For Generating the hash password
async def hash_password(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_str = pwd_context.hash(password)
    return hashed_str


async def get_token(userid):
    token = jwt.encode({"userid": userid, "exp": datetime.now() + timedelta(minutes=480)}, secret_key, algorithm)
    return token

async def verify_hash(password, hash_password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(password, hash_password)

#for validating the Authentication of JWT and returning the userid based on the token provided
async def current_user(request: Request):
    try:
        token = request.headers.get('Authorization')
        if not token:
            raise HTTPException(status_code=401, detail='Token Not found')
        token = token.replace('Bearer ','')
        payload = jwt.decode(token,secret_key,algorithm)
        return payload.get('userid')
    except JWTError:
        raise HTTPException(status_code=401, detail="Token is Inavlid")

