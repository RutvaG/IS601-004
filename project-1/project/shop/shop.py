# Import required libraries
from flask import Blueprint, request, flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.datastructures import MultiDict
from sql.db import DB
from roles.permissions import admin_permission
from shop.forms import ItemForm, CheckoutForm
# Create a blueprint instance for the shop module
shop = Blueprint('shop', __name__, url_prefix='/shop', template_folder='templates')

# Define a route for creating and updating shop items
@shop.route('/item', methods=['GET', 'POST'])
@login_required
@admin_permission.require(http_exception=403)
def create_update_item():
    form = ItemForm()
    item_id = request.args.get('id')
    item_type = 'Edit' if item_id else 'Create'

    # If the form is submitted with valid data
    if form.validate_on_submit():
        item_data = {
            'name': form.name.data,
            'description': form.description.data,
            'category': form.category.data,
            'stock': form.stock.data,
            'unit_price': form.unit_price.data,
            'visibility': 1 if form.visibility.data else 0
        }

        # If an item ID is present, update the existing item
        if item_id:
            try:
                DB.update('UPDATE shop_items SET name=%(name)s, description=%(description)s, category=%(category)s, stock=%(stock)s, unit_price=%(unit_price)s, visibility=%(visibility)s WHERE id=%(id)s', item_data)
                flash(f'{item_data["name"]} has been updated successfully.', 'success')
            except:
                flash(f'Error updating {item_data["name"]}. Please try again later.', 'danger')
        # If an item ID is not present, create a new item
        else:
            try:
                DB.insert('INSERT INTO shop_items (name, description, category, stock, unit_price, visibility) VALUES (%(name)s, %(description)s, %(category)s, %(stock)s, %(unit_price)s, %(visibility)s)', item_data)
                flash(f'{item_data["name"]} has been added to the shop.', 'success')
                form = ItemForm()  # Clear the form
            except:
                flash(f'Error adding {item_data["name"]} to the shop. Please try again later.', 'danger')

    # If an item ID is present, pre-populate the form with the item's data
    if item_id:
        try:
            item_data = DB.select_one('SELECT * FROM shop_items WHERE id=%s', item_id)
            if item_data:
                form.process(MultiDict(item_data))
            else:
                flash('Item not found.', 'danger')
        except:
            flash('Error fetching item details. Please try again later.', 'danger')

    # Render the item form template with the appropriate data
    return render_template('item.html', form=form, item_type=item_type)


from flask import Flask, request, flash, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'IS601_S_Products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    stock = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    visibility = db.Column(db.Integer)

class Cart(db.Model):
    __tablename__ = 'IS601_S_Cart'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('IS601_S_Products.id'))
    desired_quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(255))

@app.route("/admin/items/delete", methods=["GET"])
def delete():
    id = request.args.get("id")
    if id:
        try:
            Product.query.filter_by(id=id).delete()
            db.session.commit()
            flash("Deleted item", "success")
        except Exception as e:
            print("Error deleting item", e)
            flash("Error deleting item", "danger")
    return redirect(url_for("items"))

@app.route("/admin/items", methods=["GET","POST"])
def items():
    rows = []
    try:
        rows = Product.query.limit(25).all()
    except Exception as e:
        print("Error fetching items", e)
        flash("There was a problem loading items", "danger")
    return render_template("items.html", rows=rows)

@app.route("/cart", methods=["GET","POST"])
def cart():
    if not current_user.is_authenticated:
        flash("Please login to add the cart", "warning")
        return redirect(url_for('shop_list'))
    delete_all =  request.args.get('delete_all')
    item_id = request.form.get("item_id")
    id = request.form.get("id", item_id)
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if id and user_id:
        if quantity > 0:
            try:
                product = Product.query.get(id)
                if product:
                    cost = product.unit_price
                    name = product.name
                    if item_id:
                        cart_item = Cart.query.filter_by(product_id=item_id, user_id=user_id).first()
                        if cart_item:
                            cart_item.desired_quantity += quantity
                            db.session.commit()
                        else:
                            cart_item = Cart(product_id=item_id, desired_quantity=quantity, unit_price=cost, user_id=user_id)
                            db.session.add(cart_item)
                            db.session.commit()
                        flash("Added to cart", "success")
                        return redirect(url_for("cart"))
            except Exception as e:
                print("Error adding item to cart", e)
                flash("Error adding item to cart", "danger")
    elif delete_all:
        try:
            Cart.query.filter_by(user_id=user_id).delete()
            db.session.commit()
            flash("Cart is empty", "success")
        except Exception as e:
            print("Error deleting cart items", e)
            flash("Error deleting cart items", "danger")
    else:
        if id:
            flash("Quantity must be greater than zero", "danger")
        cart_items = Cart.query.filter_by(user_id=user_id).all()
        total_cost = sum([item.desired_quantity * item.unit_price for item in cart_items])
        return render_template("cart.html", cart_items=cart_items, total_cost=total_cost)

                
@shop.route("/purchase", methods=["GET","POST"])
@login_required
def purchase():
    cart = []
    total = 0
    quantity = 0
    order = {}
    try:
        DB.getDB().autocommit = False # make a transaction

        # get cart to verify
        ## UCID: ac2526, Date: Dec 21
        result = DB.selectAll("""SELECT c.id, product_id, name, c.desired_quantity, i.stock, c.unit_price as cart_cost, i.unit_price as item_cost, (c.desired_quantity * c.unit_price) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Products i on c.product_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            cart = result.rows
        # verify cart
        has_error = False
        for item in cart:
            if item["desired_quantity"] > item["stock"]:
                flash(f"Item {item['name']} doesn't have enough stock left", "warning")
                has_error = True
            print(item['cart_cost'], item["item_cost"])
            if item["cart_cost"] != item["item_cost"]:
                flash(f"Item {item['name']}'s price has changed, please refresh cart", "warning")
                has_error = True
            total += int(item["subtotal"] or 0)
            quantity += int(item["desired_quantity"])
        # check can afford
        if not has_error:
            balance = float(request.form.get('amount'))
            if total > balance:
                flash("You can't afford to make this purchase", "danger")
                has_error = True
        # create order data
        order_id = -1
        if not has_error:
            ##UCID: ac2526, Date: Dec21
            address = request.form.get('apt') + "," + request.form.get('city') + "," + request.form.get('state') + "," + request.form.get('country') + "," + request.form.get('zpcode')
            payment_method = request.form.get('paymentmethod')
            money_received = request.form.get('amount')
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            print(total, quantity, current_user.get_id(), address, payment_method, money_received, fname, lname)
            result = DB.insertOne("""INSERT INTO IS601_S_Orders (total_price, user_id, address, payment_method, money_received, first_name, last_name)
            VALUES (%s, %s, %s, %s, %s, %s, %s)""", total, current_user.get_id(), address, payment_method, money_received, fname, lname)
            if not result.status:
                flash("Error generating order", "danger")
                DB.getDB().rollback()
                has_error = True
            else:
                order_id = int(DB.db.fetch_eof_status()["insert_id"])
                order["order_id"] = order_id
                order["payment_method"] = payment_method
                order["total"] = total
                order["quantity"] = quantity
                order["fname"] = fname
                order["lname"] = lname
                order["address"] = address
        # record order history
        if order_id > -1 and not has_error:
            # Note: Not really an insert 1, it'll copy data from Table B into Table A
            result = DB.insertOne("""INSERT INTO IS601_S_OrderItems (quantity, unit_price, order_id, product_id)
            SELECT desired_quantity, unit_price, %s, product_id FROM IS601_S_Cart c WHERE c.user_id = %s""",
            order_id, current_user.get_id())
            if not result.status:
                flash("Error recording order history", "danger")
                has_error = True
                DB.getDB().rollback()
        # update stock based on cart data
        if not has_error:
            ##UCID: ac2526, Date: Dec 21
            result = DB.update("""
            UPDATE IS601_S_Products 
                set stock = stock - (select IFNULL(desired_quantity, 0) FROM IS601_S_Cart WHERE product_id = IS601_S_Products.id and user_id = %(uid)s) 
                WHERE id in (SELECT product_id from IS601_S_Cart where user_id = %(uid)s)
            """, {"uid":current_user.get_id()} )
            if not result.status:
                flash("Error updating stock", "danger")
                has_error = True
                DB.getDB().rollback()

        # empty the cart
        if not has_error:
            result = DB.delete("DELETE FROM IS601_S_Cart WHERE user_id = %s", current_user.get_id())
    
        if not has_error:
            #details = f"Spent {total} on {quantity} upgrades" # TBD
            #current_user.account.remove_points(-total, reason="purchase", details=details)
            DB.getDB().commit()
            flash("Purchase successful!", "success")
        else:
            return redirect(url_for("shop.cart"))
    except Exception as e:
        print("Transaction exception", e)
        flash("Something went wrong", "danger")
        traceback.print_exc()
    # TODO route to thank you / summary page
    # TODO add link from cart page to this route
    return render_template("order_summary.html", rows=cart, order=order)

@shop.route("/orders", methods=["GET"])
@login_required
def orders():
    if not current_user.has_role("Admin"):
        try:
            result = DB.selectAll("""
            SELECT id, total_price, created FROM IS601_S_Orders WHERE user_id = %s
            """, current_user.get_id())
            if result.status and result.rows:
                rows = result.rows
                return render_template("orders.html", rows=rows)
        except Exception as e:
            print("Error getting orders", e)
            flash("Error fetching orders", "danger")
    else:
        try:
            result = DB.selectAll("""
            SELECT o.id, o.user_id, u.username, o.total_price, o.created FROM IS601_S_Orders o, IS601_Users u WHERE o.user_id = u.id
            """)
            if result.status and result.rows:
                rows = result.rows
                return render_template("orders.html", rows=rows)
        except Exception as e:
            print("Error getting orders", e)
            flash("Error fetching orders", "danger")
    return render_template("orders.html")

@shop.route("/order", methods=["GET"])
@login_required
def order():
    if not current_user.has_role("Admin"):
        query = """
            SELECT name, oi.unit_price, oi.quantity, (oi.unit_price*oi.quantity) as subtotal 
            FROM IS601_S_OrderItems oi, IS601_S_Products i, IS601_S_Orders o 
            WHERE oi.product_id = i.id AND oi.order_id = o.id AND order_id = %s AND o.user_id = %s
        """
    else:
        query = """
            SELECT name, oi.unit_price, oi.quantity, (oi.unit_price*oi.quantity) as subtotal 
            FROM IS601_S_OrderItems oi, IS601_S_Products i, IS601_S_Orders o 
            WHERE oi.product_id = i.id AND oi.order_id = o.id AND order_id = %s
        """
    id = request.args.get("id")
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("shop.orders"))
    try:
        result = DB.selectAll(query, id, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)
            return render_template("order.html", rows=rows, total=total)
    except Exception as e:
        print("Error getting order", e)
        flash("Error fetching order", "danger")
    return redirect(url_for("shop.orders"))

@shop.route("/itemdetails", methods=["GET","POST"])
@login_required
def itemdetails():
    form = ItemForm()
    id = request.args.get("id", form.id.data or None)
    if not id:
        flash("Item not found", "danger")
        return redirect(url_for("shop.index"))
    try:
        result = DB.selectOne("SELECT id, name, description, category, stock, unit_price, visibility FROM IS601_S_Products WHERE id = %s", id)
        if result.status and result.row:
            row = result.row
            return render_template("item_details.html", row=row, form=form)
    except Exception as e:
        print("Error fetching item", e)
        flash("Item not found", "danger")
    return redirect(url_for("shop.index"))

@shop.route("/checkout", methods=["GET","POST"])
@login_required
def checkout():
    form = CheckoutForm()
    res = DB.selectOne("SELECT username FROM IS601_Users WHERE id = %s", current_user.get_id())
    if res.status:form.fname.data = res.row["username"]
    # Get all items in the user's cart
result = DB.selectAll("""SELECT c.id, c.product_id, name, c.desired_quantity, c.unit_price, (c.desired_quantity * c.unit_price) as subtotal, i.unit_price as item_cost 
        FROM IS601_S_Cart c JOIN IS601_S_Products i on c.product_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())

rows = result.rows if result.status and result.rows else []

if form.validate_on_submit():
    try:
        # Create a new order
        result = DB.insert("""
        INSERT INTO IS601_S_Orders (user_id, total_price) VALUES (%s, %s)
        """, current_user.get_id(), form.total.data)

        if result.status:
            # Get the ID of the newly created order
            order_id = result.lastrowid

            # Add each item in the user's cart to the order
            for row in rows:
                result = DB.insert("""
                INSERT INTO IS601_S_OrderItems (order_id, product_id, unit_price, quantity) VALUES (%s, %s, %s, %s)
                """, order_id, row["product_id"], row["item_cost"], row["desired_quantity"])

            # Delete all items from the user's cart
            result = DB.delete("""
            DELETE FROM IS601_S_Cart WHERE user_id = %s
            """, current_user.get_id())

            if result.status:
                flash("Order placed successfully", "success")
                import redirect; (url_for("shop.orders"))

    except Exception as e:
        print("Error placing order", e)
        flash("Error placing order", "danger")
#return render_template("checkout.html", form=form, rows=rows)
