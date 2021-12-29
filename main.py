import json
import sqlite3

from db.adaptor import SqliteAdaptor
from db.station import Station


def main():
    adaptor = SqliteAdaptor()
    file = open("korea_subway.json", encoding='utf-8')
    json_data = json.load(file)

    # 초기화
    adaptor.clean()

    print(json_data['fields'])

    for info in json_data['records']:
        print(info)

        # 기존 데이터가 존재하면 pass
        if adaptor.is_exist('STATION', 'NAME', info['역사명']):
            continue

        # INSERT
        # 역 이름 전처리
        if info['역사명'][-1] == '역':
            info['역사명'] = info['역사명'][:-1]

        # 쿼리 수행
        station_info = Station('지하철', info['역위도'], info['역경도'], info['역사명'])
        adaptor.insert_station_info(station_info)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
