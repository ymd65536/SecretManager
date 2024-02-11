import os
from lib import get_secret_value

project_id = os.environ.get("PROJECT_ID", None)
secret_id = "your-secret-id"

if project_id is None:
    raise ValueError("PROJECT_ID is not set")
else:

    # シークレットの取得
    try:
        secret_value = get_secret_value.get_secret_value(
            project_id, secret_id, "latest"
        )
        print(secret_value)
    except Exception as e:
        print(e)
