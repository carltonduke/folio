"""
Serve 3D scene defined in templates/index.html
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Serve index.html."""
    return render_template("index.html")

@app.route("/traffic")
def traffic_heatmap():
    """Serve austin_highway_incidents.html"""
    return render_template("austin_highway_incidents_map.html")


def main():
    """Driver."""
    app.run(debug=True)


if __name__ == "__main__":
    main()
