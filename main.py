import json
import sqlite3

def main():
    file = open("korea_subway.json", encoding='utf-8')
    json_data = json.load(file)

    # DB
    db = sqlite3.connect('./pubtrans4watch.db')
    cur = db.cursor()

    print(json_data['fields'])

    for info in json_data['records']:
        print(info)
        cur.execute('''
        INSERT INTO POSITION (TYPE, LATITUDE, LONGITUDE, STATION_NAME, LINE_NUM)
        VALUES (?, ?, ?, ?, ?)
        ''',
                    (1, info['역위도'], info['역경도'], info['역사명'], info['노선명'])
                    )

    cur.close()
    db.commit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
