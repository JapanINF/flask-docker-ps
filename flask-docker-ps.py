from flask import Flask, render_template
import docker

app = Flask(__name__)

@app.route('/')
def index():
    # Dockerクライアントの初期化
    client = docker.from_env()

    # 実行中のコンテナの一覧を取得
    containers = client.containers.list()

    # コンテナ情報をテンプレートに渡す
    return render_template('index.html', containers=containers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
                            
