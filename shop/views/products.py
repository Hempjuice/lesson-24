from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound

product_app = Blueprint("product_app", __name__)


PRODUCTS = {
    1: "Телефоны",
    2: "Компьютеры",
    3: "Бытовая техника",
}


@product_app.route("/", endpoint="list")
def products_list():
    return render_template("products/index.html", products=PRODUCTS)


@product_app.route("/<int:product_id>/", endpoint="details")
def product_details(product_id):
    if product_id not in PRODUCTS:
        raise NotFound(f"Не найдена категория товаров с id {product_id}")

    product_name = PRODUCTS[product_id]
    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
    )
