import os
import string
import random

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    send_file,
)
from werkzeug.utils import secure_filename

from services.data_extractor import ExtractDataService
from services.calculation import CalculationService
from services.data_writer import WriteCalculatedDataService

from services.exceptions import InputError, DataError

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"xlsx"}

app = Flask(__name__)
app.secret_key = "super secret key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SESSION_TYPE"] = "filesystem"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_filename_slug(size: int):
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"

    return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(size))


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("Ошибка загрузки")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            flash("Файл не выбран")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = get_filename_slug(8) + "_" + secure_filename(file.filename)
            fullpath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(fullpath)

            try:
                data = ExtractDataService.extract(fullpath)
                calculated_data = CalculationService.calculate(data)
                WriteCalculatedDataService.write(calculated_data, fullpath)
            except Exception as e:
                flash(f"Ошибка в загружаемом файле\n{e}")
                return render_template("index.html")

            return redirect(url_for("download_file", name=filename))

    return render_template("index.html")


@app.route("/uploads/<name>")
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
