from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')
import pycountry

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    
    #UCID: rg695 04/18/23
    query = """
            SELECT c.id, c.name, c.address, c.city, c.country, c.state, c.zip, c.website,COUNT(e.id) 
            AS employees FROM IS601_MP3_Companies c 
            LEFT JOIN IS601_MP3_Employees e ON e.company_id = c.id WHERE 1=1 """
    
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    allowed_list = [(v, v) for v in allowed_columns]
    #UCID: rg695 04/18/23
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    limit = 10
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get('limit')
    #UCID: rg695 04/18/23
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name LIKE %(name)s"
        args['name']="%"+name+"%"
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND country = %(country)s"
        args['country']="%"+country+"%"
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND state = %(state)s"
        args['state']="%"+state+"%"

    query += "GROUP BY c.id"
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and order:
        if column in allowed_columns and order in ['asc', 'desc']:
            query += f" ORDER BY {column} {order}"
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += "LIMIT %(limit)s"
        args['limit']=limit
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    elif limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Limit must be between 1 and 100", "warning")
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:

    # TODO search-9 make message user friendly
        print(e)
        flash("Error while searching for company", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_list)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = str(request.form['name'])
        address = str(request.form['address'])
        city = str(request.form['city'])
        state = str(request.form['state'])
        country = str(request.form['country'])
        zip = str(request.form['zip'])
        website = str(request.form['website'])
        # TODO add-2 name is required (flash proper error message)
        if not name:
            flash("Company name is required.", "danger")
            has_error = True
        # TODO add-3 address is required (flash proper error message)
        if not address:
            flash("Address is required.", "danger")
            has_error = True   
        # TODO add-4 city is required (flash proper error message)
        if not city:
            flash("City is required.", "danger")
            has_error = True
        # TODO add-5 state is required (flash proper error message)
        if not state:
            flash("State is required.", "danger")
            has_error = True
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        #import pycountry
        #try:

            #country_obj = pycountry.countries.get(alpha_2=country)
            #state_obj = pycountry.subdivisions.get(name=state, country_code=country_obj.alpha_2)
        #except (KeyError, AttributeError):
            #flash("Invalid state for the selected country.", "danger")
            #has_error = True
        # hint see geography.py and pycountry documentation
        
        # TODO add-6 country is required (flash proper error message)
        if not country or pycountry.countries.get(alpha_2=country)==None:
            flash("Country is required.", "danger")
            has_error = True
        # TODO add-6a country should be a valid country mentioned in pycountry
        try:
            country_obj = pycountry.countries.get(name=country)
        except KeyError:
            flash("Invalid country.", "danger")
            has_error = True
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        website = str(request.form.get('website') or '')
        # TODO add-8 zipcode is required (flash proper error message)
        if not zip:
            flash("Zipcode is required.", "danger")
            has_error = True
    
        # note: call zip variable zipcode as zip is a built in function it could lead to issues

        has_error = False # use this to control whether or not an insert occurs
        if not has_error:
            try:
        # TODO add-9 insert the company into the database (use the sql/db.py file)
                result = DB.insertOne("""
        INSERT INTO IS601_MP3_Companies
        (name, address, city, country, state, zip, website) VALUES(%s, %s, %s, %s, %s, %s, %s)
        """, name, address, city, country, state, zip, website)
                if result.status:
                    flash("Company Added Successfully", "success")
            except Exception as e:
                print(e)
                flash("An error occurred while adding the company. Please try again.", "danger")
        
    return render_template("add_company.html")
        

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id") 
    if not id:
        flash("Company ID is required", "danger")
        return redirect(url_for("company.search"))
    else:
        if request.method == "POST":
            data = {"id": id}
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            name = str(request.form.get("name"))
            address = str(request.form.get("address"))
            city = str(request.form.get("city"))
            state = str(request.form.get("state"))
            country = str(request.form.get("country"))
            zip = str(request.form.get("zip"))
            website = str(request.form.get("website"))
            # TODO edit-2 name is required (flash proper error message)
            if not name:
                flash("Name is required", "danger")
                has_error = True
            # TODO edit-3 address is required (flash proper error message)
            if not address:
                flash("Address is required", "danger")
                has_error = True
            # TODO edit-4 city is required (flash proper error message)
            if not city:
                flash("City is required", "danger")
                has_error = True
            # TODO edit-5 state is required (flash proper error message)
            if not state:
                flash("State is required", "danger")
                has_error = True
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            else:
                valid_states = [state_.name for state_ in pycountry.subdivisions.get(country_code=country)]
                if state not in valid_states:
                    flash("Please select a valid state", "danger")
                    has_error = True
            # TODO edit-6 country is required (flash proper error message)
            if not country:
                flash("Country is required", "danger")
                has_error = True
            # TODO edit-6a country should be a valid country mentioned in pycountry
            else:
                valid_countries = [country.name for country in pycountry.countries]
                if country not in valid_countries:
                    flash("Please select a valid country", "danger")
                    has_error = True
            # TODO edit-7 website is not required
            website = str(request.form.get('website') or '')
            # TODO edit-8 zipcode is required (flash proper error message)
            if not zip:
                flash("Zipcode is required", "danger")
                has_error = True
                
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies
                    SET name = %s, address = %s, city = %s, state = %s, country = %s, zip = %s, website = %s
                    WHERE id= %s""", name, address, city, state, country, zip, website, id)
                    if result.status:
                        print("Updated Record")
                        flash("Updated Record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print("An error occurred while updating your company. Please try again.")
                    flash("An error occurred while updating your company. Please try again.", "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, country, state, zipcode, website FROM IS601_MP3_Companies WHERE id= %s", (id))
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("Could not find information on requested company", "danger")

    # TODO edit-13 pass the company data to the render template
            return render_template("edit_company.html",company=row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    id = request.args.get('id')
    print ("Printing ID", id)
    args = {**request.args}
    #TODO delete-5 for all employees assigned to this company set their company_id to None/null
    if id:
        DB.update("""UPDATE IS601_MP3_Companies
                    SET company_id = %s WHERE company_id = %s""", None, id)
        
        result = DB.delete("""DELETE FROM IS601_MP3_Companies
                        WHERE id= %s""", (id,))
        del args['id']
        # TODO delete-4 ensure a flash message shows for successful delete
        if result:
            flash("Successfully Deleted Company", "success")  
        # TODO delete-6 if id is missing, flash necessary message and redirect to search                                 
    
    return redirect(url_for("company.search", **args))