import subprocess
import time
from auth import auth
from linkedin_token import linkedin_token
def start():
    subprocess.Popen(["start", "cmd", "/k", "python server.py"], shell=True)
    auth()
    time.sleep(60)
    linkedin_token()
    
# start()