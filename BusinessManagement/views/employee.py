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
    args = [] # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    allowed_list = [(v, v) for v in allowed_columns]

    #UCID: rg695 04/18/23
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    first_name = request.args.get('fn')
    last_name = request.args.get('ln')
    email = request.args.get('email')
    company= request.args.get('company')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = 10
    limit = request.args.get('limit')

    # TODO search-3 append like filter for first_name if provided
    #UCID: rg695 04/18/23
    if first_name:
        query += " AND e.first_name like %s"
        args.append(f"%{first_name}%")

    # TODO search-4 append like filter for last_name if provided
    #UCID: rg695 04/18/23
    if last_name:
        query += " AND e.last_name like %s"
        args.append(f"%{last_name}%")

    # TODO search-5 append like filter for email if provided
    #UCID: rg695 04/18/23
    if email:
        query += " AND email like %s"
        args.append(f"%{email}%")

    # TODO search-6 append equality filter for company_id if provided
    #UCID: rg695 04/18/23
    if company:
        query += f" AND company_id = {company}"

    #UCID: rg695 04/18/23
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order:
        #print(column, order)
        if column in allowed_columns and order in ['asc', 'desc']:
            query += f" ORDER BY {column} {order}"

    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    #UCID: rg695 04/18/23
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))

    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    #UCID: rg695 04/18/23
    elif limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Limit must be between 1 and 100", "warning")
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        #UCID: rg695 04/18/23
    # TODO search-10 make message user friendly
        print(e)
        flash("Error occurred while searching for employees", "danger")
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
        company = request.form.get("company")or None
        email = request.form.get("email")
        
        # TODO add-2 first_name is required (flash proper error message)
        #UCID : rg695 04/18/23
        has_error = False # use this to control whether or not an insert occurs
        if not first_name:
            has_error = True
            flash("First Name is required", "danger")
            
        
        # TODO add-3 last_name is required (flash proper error message)
        #UCID : rg695 04/18/23
        if not last_name:
            has_error = True
            flash("Last Name is required", "danger")
            #has_error = True
        
        # TODO add-4 company (may be None)
        #UCID : rg695 04/18/23
        company = request.form.get('company') or None
        
        # TODO add-5 email is required (flash proper error message)
        #UCID : rg695 04/18/23
        if not email:
            has_error = True
            flash("Email is required", "danger")
            
        
        # TODO add-5a verify email is in the correct format
        #UCID : rg695 04/18/23
        else:
            
            email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
            if not email_regex.match(email):
                has_error = True
                flash("Invalid Email Format", "danger")
        
        if not has_error:
            try:
                #TODO add-6 add query and add arguments
                #UCID : rg695 04/18/23
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees (first_name, last_name, company_id, email) 
                VALUES (%s, %s, %s, %s)
                """, first_name, last_name, company, email)
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                #UCID : rg695 04/18/23
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
            has_error = False
            # TODO edit-2 first_name is required (flash proper error message)
            if not first_name:
                has_error = True
                print("Firstname missing ")
                flash("First Name is required", "danger")
                #has_error = True

            # TODO edit-3 last_name is required (flash proper error message)
            if not last_name:
                has_error = True
                print("Lastname missing ")
                flash("Last Name is required", "danger")
                #has_error = True

            # TODO edit-4 company (may be None)
            company = request.form.get('company') or None
            print(f"company {company}")

            # TODO edit-5 email is required (flash proper error message)
            if not email:
                has_error = True
                print("Email missing ")
                flash("Email is required", "danger")
                #has_error = True

            # TODO edit-5a verify email is in the correct format
            else:
                email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
                if not email_regex.match(email):
                    has_error = True
                    print("Invalid Email")
                    flash("Invalid Email Format", "danger")
                
            if not has_error:
                try:
                    #UCID: rg695 04/18/23 
                    # TODO edit-6 fill in proper update query
                    result= DB.update("""
                    UPDATE IS601_MP3_Employees
                    SET first_name = %s, last_name = %s, email = %s, company_id = %s
                    WHERE id = %s""",first_name,last_name, email, company, id)
                    
                    if result.status:
                        print("Update employee")
                        flash("Updated Employee Record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    print(f"{e}")
                    flash("Error occurred while updating employee", "danger")
        row = {}
        try:
            #UCID: rg695 04/18/23
            # TODO edit-8 fetch the updated data 
            result = DB.selectOne("""SELECT e.first_name, e.last_name, e.email, e.company_id, 
                IF(c.name is not null, c.name, 'N/A') AS company_name
                FROM IS601_MP3_Employees AS e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id
                WHERE e.id = %s""", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash("An error occured while trying to edit employee info", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", employee=row)

@employee.route("/delete", methods=["GET"])
def delete():
    #UCID:rg695 4/18/2023
    id = request.args.get('id')
    args = {**request.args}
    if id:
        try:
            # TODO delete-1 delete employee by id
            result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id = %s", id)
            # TODO delete-4 ensure a flash message shows for successful delete
            if result.status:
                flash("Successfully deleted employee record", "success")
            # TODO delete-3 pass all argument except id to this route
            del args["id"]
            # TODO delete-2 redirect to employee search
            return redirect(url_for("employee.search", **args))
        except Exception as e:
            print(e)
            flash(f"An error occurred while deleting the employee record.", "danger")
            del args["id"]
            return redirect(url_for("employee.search", **args))
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    else:
        flash(f"Employee ID is missing", "danger")
    
    return redirect(url_for("employee.search", **args))