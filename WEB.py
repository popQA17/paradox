from threading import Thread
import random
import os
from flask import Flask, redirect, url_for, request, render_template
from flask_discord import DiscordOAuth2Session, requires_authorization
import json
import requests

app = Flask(__name__)

app.secret_key = b"%\xe0'\x01\xdeH\x8e\x85m|\xb3\xffCN\xc9g"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"  # !! Only in development environment.
app.config["DISCORD_CLIENT_ID"] = 885170335517917235
app.config["DISCORD_CLIENT_SECRET"] = "r20O7zthfY9TrWURRoIIRvCwujkBgOFd"
app.config["DISCORD_BOT_TOKEN"] = "ODg0OTg3MTAzODYyMjE4ODMy.YTgedw.lZE6yrybfVeYUTOkwTftN6PBTFU"
app.config["DISCORD_REDIRECT_URI"] = "https://paradox.popqa17.repl.co/callback"

discord = DiscordOAuth2Session(app)

HYPERLINK = '<a href="{}">{}</a>'


@app.route("/invite")
def invite():
    return redirect(
        "https://discord.com/api/oauth2/authorize?client_id=880831549120065606&permissions=8&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcallback&scope=bot%20applications.commands")


@app.route("/server")
def server():
    return redirect("https://discord.gg/9Q2k7jBRbT")


@app.route("/")
def index():
    if not discord.authorized:
        islogin = False
    else:
        islogin = True
    return render_template("index.html", islogin=islogin)


@app.route("/login/")
def login():
    return discord.create_session(scope=["identify", 'guilds'])


@app.route("/callback/")
def callback():
    data = discord.callback()
    redirect_to = data.get("redirect", "/me/")
    return redirect(redirect_to)


@app.route("/verify/", methods=["GET", "POST"])
def verify():
    if not discord.authorized:
        redirect_to = data.get("redirect", "/login")
        return redirect(redirect_to)
    else:
        user = discord.fetch_user()
        if request.method == "POST":
            code = request.form["code"]
            try:
                value = db[str(user.id)]
            except:
                return render_template("invalid.html", code=code)
            if value == code:
                db[str(user.id)] = f"verified{db[str(user.id)]}"
                return render_template("verified.html", code=code)
            else:
                return render_template("invalid.html", code=code)
        return render_template("verify.html")


@app.route("/me/")
def profile():
    if not discord.authorized:
        return redirect(url_for("login"))
    user = discord.fetch_user()
    return render_template("profile.html", username=user.name, avatar=user.avatar_url)


@app.route("/commands/")
def commands():
    return render_template("commands.html")


@app.route("/logout/")
def logout():
    discord.revoke()
    return redirect(url_for(".index"))


@app.route("/me/guilds/")
def user_guilds():
    guilds = discord.fetch_guilds()
    guild = "".join([
        f"""<div class = \"col\" style = "width: 600px; height: 300px;">
      <img style = \"border-radius: 100%; width: 100px; height: 100px;\"src = \"{g.icon_url}\"onerror=\"this.onerror=null; this.src='https://i.imgur.com/RjafEmC.gif'\"><br><h5> {g.name} </h5><br>
    <a class = "btn btn-outline-light" href = "/guild/{g.id}"> Manage </a></div>
    """
        if g.permissions.administrator else "<div style = \"display: none;\"></div>" for g in guilds])
    return """<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\"><script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script><style>/* width */::-webkit-scrollbar {
  width: 7px;
}

/* Track */


/* Handle */
::-webkit-scrollbar-thumb {
  background: white; 
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: white; 
}
</style><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\"> <body style = \" height: 100%;background-attachment: fixed;background-position: center;background-repeat: no-repeat;background-image: url(https://i.imgur.com/Lz2tRGn.png);background-size: cover;background-color: black; color: white;text-align: center;\">
<nav class="navbar navbar-expand-lg navbar-dark bg-dark" id = "navbar">
  <div class="container-fluid">
    <a class="navbar-brand" href="https://paradox-site.popqa17.repl.co">Paradox</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="/commands">Commands</a>
        </li>
	<li class="nav-item">
          <a class="nav-link" href="/me">Dashboard</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
<br><br><h1> Your guilds </h1><div class = \"row\" style = \"margin: 5%;\">""" + guild + """</div></body><br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<footer>
	Copyright, 2021, Paradox
</footer>
<br>
<br>"""


@app.route("/guild/<int:guild_id>/", methods=["POST", "GET"])
def add_to_guild(guild_id):
    guilds = discord.fetch_guilds()
    for g in guilds:
        if g.id == guild_id:
            guildname = g.name
            guildicon = g.icon_url
            guildid = g.id
            if request.method == "POST":
                newprefix = request.form["newprefix"]
                newwelcomemessage = request.form["newwelcome"]
                newmodroleid = request.form["newmodrole"]
                newwelcomechannel = request.form["newwelcomechannel"]
                with open('guild.json', 'r') as f:
                    guilde = json.load(f)
                if newprefix != "":
                    guilde[str(guildid)]["prefix"] = newprefix
                if newwelcomechannel != "":
                    guilde[str(guildid)]["welcomechannel"] = str(newwelcomechannel)
                if newwelcomemessage != "":
                    guilde[str(guildid)]["welcome"] = newwelcomemessage
                if newmodroleid != "":
                    guilde[str(guildid)]["modrole"] = str(newmodroleid)
                with open('guild.json', 'w') as f:  # writes the new prefix into the .json
                    json.dump(guilde, f, indent=4)
                return redirect(f"/guild/{g.id}")
            try:
                with open('guild.json', 'r') as f:
                    guild = json.load(f)
                prefix = guild[str(g.id)]["prefix"]
                welcome = guild[str(g.id)]["welcome"]
                welcomechannel = guild[str(g.id)]["welcomechannel"]
                modrole = guild[str(g.id)]["modrole"]
            except:
                return redirect(
                    f"https://discord.com/api/oauth2/authorize?client_id=885170335517917235&permissions=2617371734&redirect_uri=https%3A%2F%2Fparadox.popqa17.repl.co%2Fme%2Fguilds&response_type=code&scope=bot%20applications.commands%20identify&guild_id={guildid}&disable_guild_select=true")
    return render_template("guild.html", guildname=guildname, guildicon=guildicon, guilid=guildid, prefix=prefix,
                           modrole=modrole, welcome=welcome, welcomechannel=welcomechannel)


@app.route("/guild/<int:guild_id>/prefix")
@app.route("/secret/")
@requires_authorization
def secret():
    return os.urandom(16)


def keep_alive():
    '''
    Creates and starts new thread that runs the function run.
    '''


def run():
    app.run(host="0.0.0.0")


t = Thread(target=run)
t.start()