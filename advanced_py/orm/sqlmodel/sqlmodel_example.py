# Python SQLModel Example
# To run this example:
# 1. Install the required packages: pip install -r requirements.txt
# 2. Run the script: python sqlmodel_example.py

from sqlmodel import Field, SQLModel, create_engine, Session


class Hero(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int = None


engine = create_engine("sqlite:///database.db")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
        hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()


def select_heroes():
    with Session(engine) as session:
        heroes = session.query(Hero).all()
        for hero in heroes:
            print(hero)


if __name__ == "__main__":
    create_db_and_tables()
    create_heroes()
    select_heroes()
