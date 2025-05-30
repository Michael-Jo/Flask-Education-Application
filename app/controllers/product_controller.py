from flask import Blueprint, render_template, request, redirect
from ..models.models import Product, Category

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        product = Product( name=request.form["name"], price=request.form["price"], ategory_id=request.form["category_id"]  )
        product.save()
        return redirect("/")
    products = Product.get_all()
    categories = Category.get_all()
    return render_template("index.html", product_list=products, categories=categories)

@product_bp.route('/hapus/<id>')
def hapus(id):
    product = Product.get_by_id(id)
    if product:
        product.delete()
    return redirect("/")

@product_bp.route('/update/<id>', methods=["GET", "POST"])
def update(id):
    product = Product.get_by_id(id)
    categories = Category.get_all()
    if request.method == "POST":
        product.name = request.form["name"]
        product.price = request.form["price"]
        product.category_id = request.form["category_id"]
        product.save()
        return redirect("/")
    return render_template("update.html", product=product, categories=categories)
