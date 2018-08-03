import datetime

def nowtime():
    return datetime.datetime.utcnow()

def toutc(timestamp = None):
    t = timestamp
    if t is None:
        t = nowtime()
    utc = t.strftime("%Y-%m-%d %H:%M:%S m : %f, +00:00 (UTC)")
    return {'strf' : utc, 'timestamp' : t.timestamp(), 'datetime' : t}

def togmt9(timestamp = None):
    utc = toutc(timestamp)['datetime']
    gmt9 = utc + datetime.timedelta(hours=9)
    gmt9_strf = gmt9.strftime("%Y-%m-%d %H:%M:%S m : %f, +00:00 (UTC)")
    return {'strf' : gmt9_strf, 'timestamp' : gmt9.timestamp(), 'datetime' : gmt9}