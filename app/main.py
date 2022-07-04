#!/usr/local/bin/python3

from flask import Flask, render_template, request, flash, redirect
import docker
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(128)
client = docker.from_env()

@app.route("/", methods=['GET'])
def index():
    containers = client.containers.list(all=True)
    containers = sorted(containers, key=lambda x: x.name)
    volumes = client.volumes.list()
    volumes = sorted(volumes, key=lambda x: x.name)
    images = client.images.list()
    images = sorted(images, key=lambda x: x.tags[0])
    networks = client.networks.list()
    networks = sorted(networks, key=lambda x: x.name)
    return render_template("sites/index.html", containers=containers, volumes=volumes, images=images, networks=networks)

@app.route("/containers", methods=['GET', 'POST'])
def containers():

    if action := request.form.get("action", None):
        print(action)
        if action == "prune":
            try:
                client.containers.prune()
                flash('Containers successfully pruned', 'success')
            except Exception as e:
                flash(e, 'danger')

    containers = client.containers.list(all=True)
    containers = sorted(containers, key=lambda x: x.name)
    return render_template("sites/containers.html", data=containers)

@app.route("/container/<id>", methods=["GET", "POST"])
def container(id):

    if action := request.form.get("action", None):
        print(action)
        if action == "start":
            try:
                client.containers.get(id).start()
                flash('Container successfully started', 'success')
            except Exception as e:
                flash(e, 'danger')
        elif action == "restart":
            try:
                client.containers.get(id).restart()
                flash('Container successfully restarted', 'success')
            except Exception as e:
                flash(e, 'danger')
        elif action == "pause":
            try:
                client.containers.get(id).pause()
                flash('Container successfully paused', 'success')
            except Exception as e:
                flash(e, 'danger')
        elif action == "unpause":
            try:
                client.containers.get(id).unpause()
                flash('Container successfully unpaused', 'success')
            except Exception as e:
                flash(e, 'danger')
        elif action == "stop":
            try:
                client.containers.get(id).stop()
                flash('Container successfully stopped', 'success')
            except Exception as e:
                flash(e, 'danger')
        elif action == "kill":
            try:
                client.containers.get(id).kill()
                flash('Container successfully killed', 'success')
            except Exception as e:
                flash(e, 'danger')
        elif action == "remove":
            try:
                client.containers.get(id).remove()
                flash('Container successfully removed', 'success')
                return redirect("/containers")
            except Exception as e:
                flash(e, 'danger')
     
    container = client.containers.get(id)
    return render_template("sites/container.html", data=container)

@app.route("/volumes", methods=['GET', 'POST'])
def volumes():

    if action := request.form.get("action", None):
        print(action)
        if action == "prune":
            try:
                client.volumes.prune()
                flash('Volumes successfully pruned', 'success')
            except Exception as e:
                flash(e, 'danger')
    
    volumes = client.volumes.list()
    volumes = sorted(volumes, key=lambda x: x.name)
    return render_template("sites/volumes.html", data=volumes)

@app.route("/volume/<id>")
def volume(id):
    volume = client.volumes.get(id)
    return render_template("sites/volume.html", data=volume)

@app.route("/images", methods=['GET', 'POST'])
def images():

    if action := request.form.get("action", None):
        print(action)
        if action == "prune":
            try:
                client.images.prune()
                flash('Images successfully pruned', 'success')
            except Exception as e:
                flash(e, 'danger')

    images = client.images.list()
    images = sorted(images, key=lambda x: x.tags[0])
    return render_template("sites/images.html", data=images)

@app.route("/image/<id>")
def image(id):
    image = client.images.get(id)
    return render_template("sites/image.html", data=image)

@app.route("/networks", methods=['GET', 'POST'])
def networks():

    if action := request.form.get("action", None):
        print(action)
        if action == "prune":
            try:
                client.networks.prune()
                flash('Networks successfully pruned', 'success')
            except Exception as e:
                flash(e, 'danger')

    networks = client.networks.list()
    networks = sorted(networks, key=lambda x: x.name)
    return render_template("sites/networks.html", data=networks)

@app.route("/network/<id>")
def network(id):
    network = client.networks.get(id)
    return render_template("sites/network.html", data=network)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)