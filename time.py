# datetimeモジュールを使った現在の日付と時刻の取得
import datetime

dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
print(dt)  # 2021-10-29 15:58:08.356501

# 日付と時刻を構成する要素の取り出し
print(f'year: {dt.year}, month: {dt.month}, day: {dt.day}')
print(f'hour: {dt.hour}, minute: {dt.minute}, second: {dt.second}')
print(f'micro second: {dt.microsecond}')
# 出力例
#year: 2021, month: 10, day: 29
#hour: 15, minute: 58, second: 8
#micro second: 356501

# datetimeオブジェクトから日付または時刻を取り出す
d = dt.date()
print(d)  # 2021-10-29

t = dt.time()
print(t)  # 15:58:08.356501

tdy = datetime.date.today()  # 今日の日付の取得
print(tdy)  # 2021-10-29

# タイムゾーンを考慮する
dt = datetime.datetime.now()  # タイムゾーンなしで現在の日付と時刻を取得
print(dt)  # 2021-10-29 16:16:23.202059

dt = datetime.datetime.now(datetime.timezone.utc)  # タイムゾーン付きでUTCを取得
print(dt)  # 2021-10-29 07:23:14.464801+00:00
print(dt.tzinfo)  # UTC

dt = datetime.datetime.utcnow()  # タイムゾーンなしでUTCを取得
print(dt)  # 2021-10-29 07:31:41.503042

t_delta = datetime.timedelta(hours=9)  # 9時間
JST = datetime.timezone(t_delta, 'JST')  # UTCから9時間差の「JST」タイムゾーン
dt = datetime.datetime.now(JST)  # タイムゾーン付きでローカルな日付と時刻を取得
print(dt)

# timeモジュールを使った現在の日付と時刻の取得
import time

t = time.time()  # UNIX時間（1970/01/01 00:00:00からの経過時刻）を取得
dt_from_timestamp = datetime.datetime.fromtimestamp(t)
print(dt_from_timestamp)  # 2021-10-29 16:59:04.741680

c_time = time.ctime(t)  # UNIX時刻を文字列表現に変換
print(c_time)  # Fri Oct 29 16:59:04 2021

local_time = time.localtime(t)  # ローカル時刻をtime.struct_time型として取得
print(local_time)
gm_time = time.gmtime(t)  # UTC時刻をtime.struct_time型として取得
print(gm_time)
# 出力例
#time.struct_time(tm_year=2021, tm_mon=10, tm_mday=29, tm_hour=16, tm_min=59,
# tm_sec=4, tm_wday=4, tm_yday=302, tm_isdst=0)
#time.struct_time(tm_year=2021, tm_mon=10, tm_mday=29, tm_hour=7, tm_min=59,
#tm_sec=4, tm_wday=4, tm_yday=302, tm_isdst=0)

asc_time = time.asctime(local_time)  # 上のlocal_timeを文字列表現に変換
print(asc_time)  # Fri Oct 29 16:59:04 2021

dt = datetime.datetime.strptime(asc_time, '%a %b %d %H:%M:%S %Y')
print(dt)  # 2021-10-29 16:59:04