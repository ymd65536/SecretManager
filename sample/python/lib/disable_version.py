from google.cloud import secretmanager


def disable_secret_version(
    project_id: str, secret_id: str, version_id: str
) -> secretmanager.DisableSecretVersionRequest:
    """
    シークレットのバージョンを無効化する
    """

    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.disable_secret_version(request={"name": name})

    print(f"Disabled secret version: {response.name}")
