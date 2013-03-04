from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def create_db(app):
    if not app.db_session:
        # Create the engine
        engine = create_engine(app.config.get('DATABASE_URL'),
                               convert_unicode=True)

        # Create a session
        Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
        app.db_session = Session()

    return app.db_session
