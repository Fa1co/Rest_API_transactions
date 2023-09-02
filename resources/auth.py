import datetime

from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User
from flask_restful import Resource
import bcrypt
from flask_jwt_extended import create_access_token

class Authorization(Resource):
    def post(self):
        body = request.get_json()
        engine = create_engine('sqlite:///myDatabase.db')
        with Session(autoflush=False, bind=engine) as db:
            user = db.query(User).filter(User.e_mail == body['email']).first()

            if user is not None:
                authorized = bcrypt.checkpw(body['password'].encode('utf-8'), user.password)
                if not authorized:
                    return {'error': 'Email or password invalid'}, 401

            elif user is None:
                user = User(e_mail=body['email'],
                            password=bcrypt.hashpw(body['password'].encode('utf-8'), bcrypt.gensalt()))
                db.add(user)
                db.commit()

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.user_id),
                                               expires_delta=expires
                                               )
            return {'token': access_token}, 200