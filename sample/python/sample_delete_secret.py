import os
from lib import delete_secret

project_id = os.environ.get("PROJECT_ID", None)
secret_id = "your-secret-id"

if project_id is None:
    raise ValueError("PROJECT_ID is not set")
else:

    # シークレットの削除
    try:
        delete_secret.delete_secret(project_id, secret_id)
    except Exception as e:
        print(e)
