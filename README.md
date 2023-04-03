# info-collector
## 概要
Discordのwebhook urlに以下の情報を流すツール

- connpassのイベント情報
  - 3か月以内に開催されるイベントの通知
- rss feedの更新情報

## 使い方
1. redisサーバを用意する
1. config.yamlをexampleからコピーして作成する

    ```
    cp config.yaml.example config.yaml
    ```

1. config.yamlを修正する。
    - `rss_configs` に以下の情報の配列をセット
        - `feed_url` : rss feedのurl
        - `webhook_url` : 通知したいDiscordチャンネルのwebhook url
    - `connpass_configs` に以下の情報の配列をセット
        - `keyword` : 検索するイベントのキーワード
        - `webhook_url` : 通知したいDiscordチャンネルのwebhook url

1. 以下の環境変数をセットする
    - `REDIS_HOST` : redisサーバのホスト名かIPアドレス (default: `localhost`)
    - `REDIS_PORT` : redisサーバのリッスンポート (default: `6379`)
    - `REDIS_DB` : redisのDB番号 (default: `0`)

1. cronなどで定期的に以下のコマンドを実行する

    ```
    cd <git repository path> && python main.py
    ```
