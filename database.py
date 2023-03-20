from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .config import current_config

from .models.models import *
db_url_key = "DATABASE_URI"
engine = create_engine(current_config().DATABASE_URI)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from .models.models import Base, User, Transaction

    Base.metadata.create_all(bind=engine)
