import sys
import traceback
from flask import Flask, request, jsonify, send_from_directory

from agent import Agent

app = Flask(__name__, static_folder="static", static_url_path="")

agent = Agent()


@app.route("/", methods=["GET"])
def index():
    return send_from_directory("static", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True)

        user_input = data.get("message", "").strip()

        if not user_input:
            return jsonify({
                "success": False,
                "response": "Empty message."
            }), 400

        response = agent.run(user_input)

        return jsonify({
            "success": True,
            "response": response
        })

    except Exception:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "response": traceback.format_exc()
        }), 500


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


def run_cli():
    print("=" * 60)
    print("AI Agent")
    print("=" * 60)
    print("Type 'exit' to quit.\n")

    cli_agent = Agent()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            break

        try:
            response = cli_agent.run(user_input)
            print(f"\nAgent: {response}\n")

        except Exception:
            traceback.print_exc()


if __name__ == "__main__":
    if "--cli" in sys.argv:
        run_cli()
    else:
        app.run(host="0.0.0.0", port=5000)