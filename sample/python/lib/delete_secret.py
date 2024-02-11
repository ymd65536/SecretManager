from google.cloud import secretmanager


def delete_secret(project_id, secret_id):
    """
    シークレットの削除
    """
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_path(project_id, secret_id)
    response = client.delete_secret(request={"name": name})

    print("Deleted secret: {}".format(response))
