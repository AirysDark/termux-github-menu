
import requests
from rich.prompt import Prompt
from devops_enterprise.core.config import save_accounts, load_accounts

CLIENT_ID="Iv1.0000000000000000"

def execute():
    print("Starting OAuth device flow")
    r=requests.post("https://github.com/login/device/code",
        data={"client_id":CLIENT_ID,"scope":"repo"},
        headers={"Accept":"application/json"}).json()
    print("Visit:",r["verification_uri"])
    print("Code:",r["user_code"])
