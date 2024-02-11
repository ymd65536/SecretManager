from google.cloud import secretmanager
import google_crc32c  # type: ignore


def get_secret_value(project_id: str, secret_id: str, version: str) -> str:

    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_version_path(project_id, secret_id, "latest")
    response = client.access_secret_version(request={"name": name})

    return response.payload.data.decode("UTF-8")


def access_secret_version(
    project_id: str, secret_id: str, version_id: str
) -> secretmanager.AccessSecretVersionResponse:
    """
    バージョンを指定してシークレットの値を取得する
    """

    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    response = client.access_secret_version(request={"name": name})

    crc32c = google_crc32c.Checksum()
    crc32c.update(response.payload.data)
    if response.payload.data_crc32c != int(crc32c.hexdigest(), 16):
        print("Data corruption detected.")
        return response

    payload = response.payload.data.decode("UTF-8")
    print(f"Plaintext: {payload}")
