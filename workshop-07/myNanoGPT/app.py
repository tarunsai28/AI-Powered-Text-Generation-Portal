
import os
import sys
import subprocess

from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")


def clean_generated_text(raw_output):
    """Remove nanoGPT startup messages from generated text."""

    lines = raw_output.splitlines()

    filtered = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith((
            "Overriding:",
            "number of parameters:",
            "Loading meta",
            "No meta.pkl",
            "WARNING:",
        )):
            continue

        if stripped == "---------------":
            continue

        filtered.append(line)

    return "\n".join(filtered).strip()


@app.route("/generate", methods=["GET"])
def generate():

    try:
        command = [
            sys.executable,
            "sample.py",
            "--out_dir=out_twitter",
            "--device=cpu",
            "--num_samples=1",
            "--max_new_tokens=150",
            "--temperature=0.8",
        ]

        result = subprocess.run(
            command,
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=180,
        )

        if result.returncode != 0:
            app.logger.error(result.stderr)

            return jsonify({
                "error": "Model generation failed."
            }), 500

        generated_text = clean_generated_text(result.stdout)

        if not generated_text:
            return jsonify({
                "error": "Model returned empty text."
            }), 500

        return jsonify({
            "generated_text": generated_text
        })

    except subprocess.TimeoutExpired:
        return jsonify({
            "error": "Generation timed out."
        }), 504

    except Exception:
        app.logger.exception("Generation error")

        return jsonify({
            "error": "Unexpected server error."
        }), 500


if __name__ == "__main__":
    print("Starting Flask at http://127.0.0.1:5000")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False
    )
