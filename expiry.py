from configparser import ConfigParser
from datetime import datetime
config=ConfigParser()
config.read("codes.ini")
expiry_sec=int(config["LINKEDIN"]["expiry_sec"])
expiry_date = datetime.fromtimestamp(expiry_sec)
present_date=datetime.today()
# new_date = resulting_date.replace(year=2026)
# print(present_date)
# # 3. Print the result
# print(expiry_date)
def is_expired():
    if(present_date>expiry_date):
        # print("expired")
        return True
    else:
        # print("not expired")
        return False
# check_expiry()