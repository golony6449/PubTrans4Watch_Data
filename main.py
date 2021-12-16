import json
import sqlite3


def main():
    file = open("korea_subway.json", encoding='utf-8')
    json_data = json.load(file)

    # DB
    db = sqlite3.connect('./pubtrans4watch.db')
    cur = db.cursor()

    # 초기화
    cur.execute('''
    DELETE FROM POSITION
    ''')

    print(json_data['fields'])

    for info in json_data['records']:
        print(info)

        # 기존 데이터가 존재하면 pass
        cur.execute('SELECT * FROM POSITION WHERE STATION_NAME=:station_name', {'station_name': info['역사명']})
        if len(cur.fetchall()) != 0:
            continue

        # INSERT
        # 역 이름 전처리
        if info['역사명'][-1] == '역':
            info['역사명'] = info['역사명'][:-1]

        # 쿼리 수행
        cur.execute(
            '''
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
