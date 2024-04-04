from db import Connection


def main():
    db = Connection('data/db/Cereal.db')
    db.connect()
    print(db.is_connected())
    db.disconnect()
    print(db.is_connected())


if __name__ == '__main__':
    main()
