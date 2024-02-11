import os
from lib import create_secret

project_id = os.environ.get("PROJECT_ID", None)
secret_id = "your-secret-id"

if project_id is None:
    raise ValueError("PROJECT_ID is not set")
else:

    # シークレットの作成
    try:
        create_secret.create_secret(project_id, secret_id)
    except Exception as e:
        print(e)
