'''Model definitions'''
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# imgbb.com

db = SQLAlchemy()

class User(db.Model):
    '''Defines users table.'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(255), nullable=False)

    pins = relationship("Pin", back_populates="owner")
    boards = relationship("Board", back_populates="owner")

    @property
    def password(self):
        '''returns the hashed password'''
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        '''verifies the password matches the hashed password'''
        return check_password_hash(self.password, password)

class Pin(db.Model):
    '''Describes pins table'''
    __tablename__ = 'pins'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    ownerId = db.Column(db.Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="pins")

    comments = relationship("Comment", back_populates="pin")
    labels = relationship("Label", back_populates="pin")

class Board(db.Model):
    '''Describes boards table'''
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)

    ownerId = db.Column(db.Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="pins")

    boardPins = relationship("BoardPin", back_populates="board")

class BoardPin(db.Model):
    '''Describes boardPins table. Each board has 0 or more pins'''
    __tablename__ = 'boardPins'
    id = db.Column(db.Integer, primary_key=True)

    #Will have to test this. Not sure if this should be relationshipped.
    # Should pinID be linked? or just straight integer.
    # pinId = db.Column(db.Integer, ForeignKey("pins.id"))
    # pin = relationship("Pin", back_populates="pins")
    pinId = db.Column(db.Integer, nullable=False)

    boardId = db.Column(db.Integer, ForeignKey("boards.id"))
    board = relationship("Board", back_populates="boardPins")

class Comment(db.Model):
    '''Describes comment table. Each Pin has 0 or more comments.'''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), nullable=False)

    pinId = db.Column(db.Integer, ForeignKey("pins.id"))
    pin = relationship("Pin", back_populates="comments")

class Label(db.Model):
    '''Describes labels (tags) table. Each Pin has 0 or more labels.'''
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(15), nullable=False)

    pinId = db.Column(db.Integer, ForeignKey("pins.id"))
    pin = relationship("Pin", back_populates="labels")
