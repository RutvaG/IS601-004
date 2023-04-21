import re
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    #UCID: rg695 04/18/23
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT e.id , e.first_name, e.last_name, e.email, e.company_id, IF(name is not null, name,'N/A') as company_name
            FROM IS601_MP3_Employees AS e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    allowed_list = [(v, v) for v in allowed_columns]
    #UCID: rg695 04/18/23
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    first_name = request.args.get('fn')
    last_name = request.args.get('ln')
    email = request.args.get('email')
    company= request.args.get('company')
    limit = 10
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit')
    # TODO search-3 append like filter for first_name if provided
    if first_name:
        query += " AND first_name LIKE %(first_name)s"
        args['first_name']="%"+first_name+"%"
    # TODO search-4 append like filter for last_name if provided
    if last_name:
        query += " AND last_name LIKE %(last_name)s"
        args['last_name']="%"+last_name+"%"
    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND email LIKE %(email)s"
        args['email']="%"+email+"%"
    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += " AND company_id = %(company)s"
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order:
        print(column, order)
        if column in allowed_columns and order in ['asc', 'desc']:
            query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100

    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    elif limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Limit must be between 1 and 100", "warning")
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
    # TODO search-10 make message user friendly
        print(e)
        flash("Error occurred while searching for employees", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_list)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        #UCID : rg695 04/18/23
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        company = request.form.get("company")
        email = request.form.get("email")
        
        # TODO add-2 first_name is required (flash proper error message)
        has_error = False # use this to control whether or not an insert occurs
        if not first_name:
            flash("First Name is required", "danger")
            has_error = True
        
        # TODO add-3 last_name is required (flash proper error message)
        if not last_name:
            flash("Last Name is required", "danger")
            has_error = True
        
        # TODO add-4 company (may be None)
        company = request.form.get('company') or None
        
        # TODO add-5 email is required (flash proper error message)
        if not email:
            flash("Email is required", "danger")
            has_error = True
        
        # TODO add-5a verify email is in the correct format
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email format", "danger")
            has_error = True
        
        if not has_error:
            try:
                #TODO add-6 add query and add arguments
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees (first_name, last_name, company_id, email) 
                VALUES (%s, %s, %s, %s)
                """, first_name, last_name, company, email)
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                print(e)
                flash("An error occurred while adding employee", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    #UCID: rg695 04/18/23
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Company ID not found", "danger")
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            company = request.form.get("company")
            email = request.form.get("email")
            
            # TODO edit-2 first_name is required (flash proper error message)
            if not first_name:
                flash("First Name is required", "danger")
                has_error = True

            # TODO edit-3 last_name is required (flash proper error message)
            if not last_name:
                flash("Last Name is required", "danger")
                has_error = True

            # TODO edit-4 company (may be None)
            if company == "":
                company = None

            # TODO edit-5 email is required (flash proper error message)
            if not email:
                flash("Email is required", "danger")
                has_error = True

            # TODO edit-5a verify email is in the correct format
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                flash("Invalid email format", "danger")
                has_error = True
            
                
            if not has_error:
                try:
                    #UCID: rg695 04/18/23 
                    # TODO edit-6 fill in proper update query
                    query= """
                    UPDATE IS601_MP3_Employees
                    SET first_name = %s, last_name = %s, email = %s, company = %s
                    WHERE id = %s"""
                    args = {
                        "id": id,
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "company": company
                    }
                    result = DB.update(query, args)
                    
                    if result.status:
                        flash("Updated Employee Record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash("Error occurred while updating employee", "danger")
        row = {}
        try:
            #UCID: rg695 04/18/23
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("""SELECT e.first_name, e.last_name, e.email, e.company_id, 
                IF(c.name is not null, c.name, N/A') AS company_name
                FROM IS601_MP3_Employees AS e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id
                WHERE e.id = %s""", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("An error occured while trying to edit employee info", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", emplyoee = row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    #UCID: rg695 04/18/23
    id = request.args.get('id')
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM employees WHERE id = %s", id)

            if result.status:
                flash("Employee deleted successfully", "success")
        except Exception as e:
            flash("An error occurred while deleting employee record", "danger")
        del args["id"]
        
    return redirect(url_for('employee.search', **args))