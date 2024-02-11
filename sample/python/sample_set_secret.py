import os
from lib import set_secret

project_id = os.environ.get("PROJECT_ID", None)
secret_id = "your-secret-id"

if project_id is None:
    raise ValueError("PROJECT_ID is not set")
else:

    # シークレットの設定
    try:
        secret_path = set_secret.add_secret_version(
            project_id, secret_id, "sample")
        print(secret_path)
    except Exception as e:
        print(e)
