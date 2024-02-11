# SecretManager

Google CloudのSecretManagerを操作する

## Package install

```bash
pip install google-cloud-secret-manager google_crc32c
```

## SetUp

認証するために、以下のコマンドを実行します。

```bash
gcloud auth login
```

プロジェクトの一覧を表示します。

```bash
# プロジェクトの一覧を取得
gcloud projects list
```

プロジェクトを選択します。

```bash
# プロジェクトを選択
gcloud config set project <PROJECT_ID>
```

## APIの有効化

```bash
gcloud services enable secretmanager.googleapis.com
```

## 環境変数をセット

```bash
export PROJECT_ID=<PROJECT_ID>
```
