from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session

tables = {"Amenity": Amenity, "City": City, "Place": Place,
          "State": State, "Review": Review, "User": User}


class DBStorage:
    __session = None
    __engine = None

    def __init__(self):
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dic = {}
        for table in tables:
            if cls is None or cls is tables[table] or table is tables:
                objs = self.__session.query(tables[table]).all()
                for obj in objs:
                    key = obj.__class__.__name__+'.'+obj.id
                    dic[key] = obj
        return dic

    def new(self, obj):
        """Creates new obj session"""
        self.__session.add(obj)

    def save(self):
        """Commit's all sessions"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create session"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session

    def close(self):
        """Remove session"""
        self.__session.remove()
