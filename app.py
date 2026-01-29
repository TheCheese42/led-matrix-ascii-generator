from flask import Flask, render_template, request

from matrix_generator import generate, mapping

app = Flask(__name__)


MonthDataType = dict[str, list[list[dict[str, str]]]]


@app.route("/")
def home() -> str:
    context = {"allowed_symbols": "".join(mapping.keys())}
    return render_template("index.html", **context)


@app.route("/gen")
def gen() -> str:
    if text := request.args.get("t"):
        try:
            return generate(text)
        except KeyError:
            unsupported_characters = list(set([
                char for char in text if char not in mapping
            ]))
            return (
                f"Unsupported characters: {', '.join(unsupported_characters)}"
            )
    return "Nothing to convert"
