import datetime
today = datetime.datetime.now()
yesterday = datetime.datetime.now() - datetime.timedelta(1)
tomorrow = datetime.datetime.now() + datetime.timedelta(1)
print("Yesterday : ", yesterday)
print("Today     : ", today)
print("Tomorrow  : ", tomorrow)