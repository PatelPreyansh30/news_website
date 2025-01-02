from base import db

class UserVO(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column('first_name', db.String(255), nullable= False)
    last_name = db.Column('last_name', db.String(255), nullable= False)
    email = db.Column('email', db.String(255), nullable= False)
    password = db.Column('password', db.String(255), nullable= False)
    is_admin = db.Column('is_admin', db.Boolean(), default=0)

    def as_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'is_admin': self.is_admin
        }

db.create_all()