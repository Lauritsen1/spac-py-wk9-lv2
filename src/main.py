from db import DB


def main():
    db = DB('data/Cereal.db')
    db.connect()
    print(db.is_connected())
    db.disconnect()
    print(db.is_connected())


if __name__ == '__main__':
    main()
