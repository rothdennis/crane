from flask import Flask
from flask import render_template

import docker

app = Flask(__name__)
client = docker.from_env()

@app.route("/containers")
@app.route("/")
def containers():
    containers = client.containers.list(all=True)
    containers = sorted(containers, key=lambda x: x.name)
    return render_template("sites/containers.html", data=containers)

@app.route("/volumes")
def volumes():
    volumes = client.volumes.list()
    volumes = sorted(volumes, key=lambda x: x.name)
    return render_template("sites/volumes.html", data=volumes)

@app.route("/images")
def images():
    images = client.images.list()
    images = sorted(images, key=lambda x: x.tags[0])
    return render_template("sites/images.html", data=images)

@app.route("/networks")
def networks():
    networks = client.networks.list()
    networks = sorted(networks, key=lambda x: x.name)
    return render_template("sites/networks.html", data=networks)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)