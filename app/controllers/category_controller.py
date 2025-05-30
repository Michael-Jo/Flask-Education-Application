from flask import Blueprint, render_template, request, redirect
from ..models.models import Category

category_bp = Blueprint('category_bp', __name__, url_prefix='/kategori')

@category_bp.route('/', methods=["GET", "POST"])
def kategori():
    if request.method == "POST":
        kategori = Category(name=request.form["name"])
        kategori.save()
        return redirect("/kategori")
    kategori_list = Category.get_all()
    return render_template("kategori.html", kategori_list=kategori_list)

@category_bp.route('/update/<id>', methods=["GET", "POST"])
def kategori_update(id):
    kategori = Category.get_by_id(id)
    if request.method == "POST":
        kategori.name = request.form["name"]
        kategori.save()
        return redirect("/kategori")
    return render_template("update.html", kategori=kategori)

@category_bp.route('/hapus/<id>')
def kategori_hapus(id):
    kategori = Category.get_by_id(id)
    if kategori:
        kategori.delete()
    return redirect("/kategori")
