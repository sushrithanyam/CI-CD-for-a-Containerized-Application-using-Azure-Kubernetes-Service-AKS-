from flask import Flask, render_template

app = Flask(__name__)

dashboard = {
    "deployments": 45,
    "pods": 12,
    "uptime": "99.9%",
    "pipelines": 5
}

recent_deployments = [
    {"service": "frontend", "version": "v1.2.0", "status": "Success"},
    {"service": "backend", "version": "v2.0.1", "status": "Success"},
    {"service": "payments", "version": "v1.4.3", "status": "Running"},
]

team = [
    {"name": "Sarah Wilson", "role": "DevOps Engineer"},
    {"name": "John Smith", "role": "Cloud Architect"},
    {"name": "Emily Davis", "role": "SRE Engineer"}
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard=dashboard,
        deployments=recent_deployments,
        team=team
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)