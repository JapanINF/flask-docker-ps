from flask import Flask, render_template
import docker

app = Flask(__name__)


class container_info:
    def __init__(self, name, image, state, status):
        self.name = name
        self.image = image
        self.state = state
        self.status = status


@app.route("/")
def index():
    # Dockerクライアントの初期化
    client = docker.APIClient(base_url="unix://var/run/docker.sock")

    # 実行中のコンテナの一覧を取得
    containers = client.containers()
    container_status_list = []
    for container in containers:
        info = container_info(
            container["Names"][0],
            container["Image"],
            container["State"],
            container["Status"],
        )
        print(container["Names"][0])
        container_status_list.append(info)

    # コンテナ情報をテンプレートに渡す
    return render_template("index.html", containers=container_status_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
