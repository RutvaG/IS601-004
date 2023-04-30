<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Rutva Gandhi (rg695)</td></tr>
<tr><td> <em>Generated: </em> 4/28/2023 5:19:26 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/rg695" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234953038-544df685-7fe2-481d-a95c-7db573fc70a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in the image it shows the URL from heroku dev, it also<br>shows the index page where it shows the message with my name ucid<br>and class section. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234953607-9dbcd056-4ae0-4115-87de-d05b9b160667.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><a href="https://is601-rg695-mp3-dev.herokuapp.com/company/search">https://is601-rg695-mp3-dev.herokuapp.com/company/search</a>  Here is the relevant URL for company search with the screenshot<br>attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234953959-b7455eb8-048e-4ee9-ac71-634ab2d91edb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><a href="https://is601-rg695-mp3-dev.herokuapp.com/company/add">https://is601-rg695-mp3-dev.herokuapp.com/company/add</a> Here is the relevant URL for company add with the screenshot attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234954222-90a8b490-b32b-4cbf-8614-14df56b29d28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><a href="https://is601-rg695-mp3-dev.herokuapp.com/employee/search">https://is601-rg695-mp3-dev.herokuapp.com/employee/search</a> Here is the relevant URL for employee search with the screenshot attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234954477-944f9b93-76e5-4e16-8f4a-b69bae10232e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><a href="https://is601-rg695-mp3-dev.herokuapp.com/employee/add">https://is601-rg695-mp3-dev.herokuapp.com/employee/add</a> Here is the relevant URL for employee add with the screenshot attached<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234954789-feb2dbb1-10fd-4bb9-8a4a-f928dc1ca268.png"/></td></tr>
<tr><td> <em>Caption:</em> <p><a href="https://is601-rg695-mp3-dev.herokuapp.com/admin/import">https://is601-rg695-mp3-dev.herokuapp.com/admin/import</a> Here is the relevant URL for admin import with the screenshot attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234955617-4073cbb1-6a2b-411b-ad07-383aceff63ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP3_Companies table with visible and populated data with the UCID visible on left<br>side<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234955924-b5074d6d-ca43-4802-9dcd-704562693c32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP3_Employees table with visible and populated data with the UCID visible on left<br>side<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235252841-6e1cc524-c644-4036-af2d-2e717798a2f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the code snippet where it checks if the file is a<br>.csv file otherwise reject with a flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235253264-21ff0fb5-1b21-4855-b951-c21cf537e139.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet code where csv file reads from the provided stream<br>as a dict, employee and company is ectracted as a dict to respective<br>lists.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235253762-a3c7d3f8-60e4-4df6-9f7f-d854297ce946.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for all flash messages for TODO 5-8<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235254043-95291db7-7a91-4932-9143-dbe5442f4eb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where data.csv file is choosed to import<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235254209-6c31a2bd-1073-4fc1-9251-155239b074ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where it shows message for number of companies and<br>employees were inserted or updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235254572-17d686bf-458b-4757-921c-2e1e48298371.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where it gives error when try to import file<br>other then .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235254852-20c52e60-1b55-4ce9-9a77-f606125d5ebe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where it gives and error message when we dont<br>choose any file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235255735-f6aa11a5-87d2-4ae0-a8a5-112bd30e01d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing some employee data was uploaded and UCID and<br>DB name visible on left side<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235255553-bea9f55a-f883-4c51-906f-c473f0b8e01e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing some company data was uploaded and UCID and<br>DB name visible on left side <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234960352-7fc585f4-84ef-40c9-8d31-1ddb7c56504c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code here is retriving first_name, last_name, company (id), email with the route and<br>UCID and date is mentioned <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234961141-d1467aa0-a2e6-4293-b7a5-6640e1a3d508.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the screenshot where first_name is required and flashing proper error message<br>if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234961564-db670552-a264-43d5-9a3f-d20970aedef4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the screenshot where last_name is required and flashing proper error message<br>if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234961787-3ecd17fd-0237-4854-b69a-5e5e3cb2b965.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the company where it doesn&#39;t require a flash and can be<br>empty/None<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234962173-bf3749c3-24e6-42ec-94b8-6bf2a7f0ef0b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in the screenshot where email is required with flashing proper error message<br>if email is missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234962566-972d91ca-8794-4d33-8fca-17f6176cee9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the Email format which is verified and works<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234963088-5872b570-6d26-48d8-9afc-ea768ede1d9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the Proper INSERT query with visible along with the data being<br>passed in and also it flashes that &quot;Created Employee Record&quot;, &quot;success&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234963622-fc526478-2974-4d96-b169-c3d4d545d96d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the Except block where it has a user-friendly message flashed and<br>a print(e) of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234964105-e46574e6-164d-4d31-8272-b3391cc9efc7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows filled in valid data with firstname, lastname, email, and company<br>name prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234964474-0dfe2f16-2a7b-4d42-934b-11e91b534546.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows success message &quot;Created Employee Record&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234964888-3ca0ebae-45d6-4569-9760-c92c586f9004.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows first_name error message which says &quot;First Name is required&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234965160-5316bd64-d1a6-4b8a-8a89-33a45792fa91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows last_name error message which says &quot;Last Name is required&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234965535-b34d89c4-7103-4f74-8708-cc1f485c19ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows email error message which says &quot;Email is required&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234966314-7e2dec86-3d3d-429f-b3f9-132441ea5a9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows the data of the new employee we previously with the<br>help of search i searched the name where it shows all data with<br>that name and UCID and DB name is visible on left side<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234967183-38f65fdd-f5f5-4d99-8f51-f4d5bd9f29d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the SELECT query which is  filled in properly to pull<br>employee id, first_name, last_name, email, company_id, company_name via a LEFT JOIN with allowed_columns<br>and allowed_list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234967808-37933074-b4b7-48e4-ac86-cf26c6d963aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it retrieves values for the first_name, last_name, email, company, column, order, and<br>limit parameters. The request.args.get() method is used to retrieve these values from the<br>query string of the request URL. The limit parameter is initially set to<br>a default value of 10, but its value is updated if a limit<br>parameter is passed in the request arguments. These values will be used later<br>to filter, sort, and limit the results of a SQL query.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234968044-05d7c027-e5fc-4154-b56f-05d83816a3c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it checks if a value has been provided for the first_name parameter<br>in the request arguments. If a value is present, it appends a SQL<br>WHERE clause to the query string, filtering the results by the first_name column<br>of the IS601_MP3_Employees table.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234968467-de929568-1cd3-4911-9671-46a0916ef604.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it checks if a value has been provided for the last_name parameter<br>in the request arguments. If a value is present, it appends a SQL<br>WHERE clause to the query string, filtering the results by the last_name column<br>of the IS601_MP3_Employees table. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234968888-18b0eb50-d3fb-46b6-a770-145d6ced1340.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it checks if a value has been provided for the email parameter<br>in the request arguments. If a value is present, it appends a SQL<br>WHERE clause to the query string, filtering the results by the email column<br>of the IS601_MP3_Employees table.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234969066-4be8dfce-319d-4b27-9d8f-20e769d8484b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows how the append equality filter works for company_id if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234969330-fc16719b-504e-4f1a-a2b9-77fa71fe2067.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet checks if a column and its corresponding order are provided<br>as arguments, and if so, ensures that they are valid options within the<br>allowed columns and order options (&#39;asc&#39;, &#39;desc&#39;). If the column and order are<br>valid, it appends a sorting clause to the query string that will be<br>executed on the database. The sorting clause is constructed using the provided column<br>and order values, and added to the end of the query string using<br>the ORDER BY statement.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234970098-f63f93f9-b860-4143-a932-c743d418c1c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it checks if a limit parameter has been passed to the function<br>and ensures that the value of the limit is between 1 and 100.<br>If the limit is valid, it appends a SQL LIMIT clause to the<br>query and adds the limit value to the function arguments. The default limit<br>value is 10 if no limit parameter is provided.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234973110-98035146-1799-4f9f-ae5c-1c2eeaf5b949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet checks if the limit argument is provided and if it<br>is a valid number between 1 and 100. If limit is not a<br>valid number or if it is outside the allowed bounds, a warning message<br>is flashed to the user interface with the text &quot;Limit must be between<br>1 and 100&quot;.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234973519-595d755e-4308-4a5d-925b-e72f8ac774f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet is an exception handler that is triggered if an error<br>occurs while searching for employees. It prints the exception message to the console<br>for debugging purposes, but it also provides a user-friendly error message using the<br>flash function. The error message that is displayed to the user is &quot;Error<br>occurred while searching for employees&quot;. This message informs the user that there was<br>a problem with the search operation and advises them to try again later.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234973978-e23fa98e-468f-4e9c-bd22-fb80531dcb2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows the first_name searched as Lenna where it shows 3 results<br>with the name and the data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234974402-331e6b6e-e02f-423a-a322-ce5846bc537a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows the last_name searched as Ruta where it shows only 1<br>results with the correct data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234974830-2dc2da7a-2e1a-4818-9f17-bdba4b384fb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows the email searched as <a href="mailto:&#x6b;&#114;&#x69;&#x73;&#64;&#103;&#x6d;&#97;&#105;&#108;&#46;&#x63;&#x6f;&#x6d;">&#x6b;&#114;&#x69;&#x73;&#64;&#103;&#x6d;&#97;&#105;&#108;&#46;&#x63;&#x6f;&#x6d;</a> where it shows only 1<br>results with the correct data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234975115-12ba4d84-9009-4447-a77b-500ea6f3ab4f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows the company name searched as Acme Supply Co where it<br>shows only 2 results with the correct data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234976840-ba230b54-fc0b-4de0-a75d-2abd2d4957a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows one asc filter applied with email as selected column<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234976591-2c7d6754-8fd3-4764-ab76-ab7908c87a60.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows one desc filter applied with first name column<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234977553-b86d9dc9-7215-489e-9d34-a11649939a88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet retrieves the value of the id argument from the GET<br>request query parameters using request.args.get(&quot;id&quot;). If id is not found in the request,<br>a danger flash message is generated to inform the user that the company<br>ID was not found. If id is present, the code checks if the<br>request method is POST, indicating that the user has submitted a form to<br>update the company information.  Here retrieving the form data for first_name, last_name,<br>company, and email. These values are extracted from the POST request using request.form.get()<br>and assigned to their respective variables (first_name, last_name, company, and email). This allows<br>the server-side code to access the updated form data and process it accordingly.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234978840-a8805726-47c8-4d7f-badb-048343e07e40.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet checks if first_name is empty or not provided in the<br>form data. If first_name is missing, it sets the has_error variable to True<br>to indicate that an error occurred. It also generates a danger flash message<br>that informs the user that the &quot;First Name is required&quot; and prompts them<br>to provide the missing information. This helps ensure that the user provides all<br>necessary information to complete the form and prevents errors or unexpected behavior caused<br>by missing data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234979144-af82bdf6-c35b-46ab-880c-b81ee6f68b85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet checks if last_name is empty or not provided in the<br>form data. If last_name is missing, it sets the has_error variable to True<br>to indicate that an error occurred. It also generates a danger flash message<br>that informs the user that the &quot;Last Name is required&quot; and prompts them<br>to provide the missing information. This helps ensure that the user provides all<br>necessary information to complete the form and prevents errors or unexpected behavior caused<br>by missing data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234979550-7efdda12-3935-4c9a-bec8-892efd80f0ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet retrieves the value of the company field from the form<br>data using request.form.get(&#39;company&#39;). The resulting value of company is printed to the console<br>for debugging purposes using print(f&quot;company {company}&quot;).  The or operator is used to<br>provide a default value of None in these cases, so that the database<br>record is updated with a NULL value in the company field if the<br>user does not provide a value.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234980157-5ef8b5e8-db4a-456b-b06b-b1d164b6a0c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet checks if email is empty or not provided in the<br>form data. If email is missing, it sets the has_error variable to True<br>to indicate that an error occurred. It also generates a danger flash message<br>that informs the user that the &quot;Email is required&quot; and prompts them to<br>provide the missing information. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234980485-11360d4d-df50-4cba-9d42-a588e43d9e77.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code is the snippet of the proper query with visible data from<br>IS601_MP3_Employees<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234980865-6d39409c-1da9-4ada-bac0-2f89d7b154e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet catches any exceptions that occur during the processing of the<br>form data and generates a danger flash message that informs the user that<br>an &quot;Error occurred while updating employee&quot; and prompts them to try again later.<br>It also prints the exception message to the console for debugging purposes using<br>print(f&quot;{e}&quot;).<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234981783-e7243a56-2290-439b-86f8-a7c4914a752c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code is the snippet of the proper SELECT query with visible data<br>from IS601_MP3_Employees joining IS601_MP3_Companies<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234982128-87ec63e3-81e4-456d-b6a6-e6478a51447d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code snippet catches any exceptions that occur during the processing of the<br>form data and generates a danger flash message that informs the user that<br>an &quot;An error occured while trying to edit employee info&quot; and prompts them<br>to try again later. the code passes the row object containing the data<br>for the employee being edited to the render_template() function, which generates the HTML<br>for the &quot;edit_employee.html&quot; page. The data is used to pre-populate the form fields<br>with the existing employee data, so that the user can make changes to<br>the fields as needed. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234983367-e6f0af03-5a01-4336-8ceb-fe649f4405ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the data on the website where it shows<br>the data where we can edit. I will be editing &quot;Kris Marrier&quot; data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234983901-efbcd64f-7104-4d5c-ad4e-5e37196f37bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where i am editing Firstname and email of the<br>employee and when i click on save Employee it flashes the message saying<br>Updated Employee record <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234984543-bd880ada-e519-492e-8c0b-d325d3508245.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the data of where i will be editing data of Mitsue<br>Tollner. with UCID and DB name mentioned in the left<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/234985200-9d2d3d31-eb32-442e-bb05-c2cfc0dc0bf5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the data of where i edited data of Mitsue Tollner to<br>Mike Denim. with UCID and DB name mentioned in the left<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235025832-adcb8fec-d89e-43bf-b85a-8a5f1f475653.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here code snippet checks if the request method is &quot;POST&quot; and if so,<br>retrieves form data for name, address, city, state, country, zip, and website using<br>the Flask framework.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235029565-6dcea351-ad6a-41ef-93e8-1c991ec19265.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here code snippet shows that the if not name: statement checks if name<br>is false, meaning it is either an empty string or None. If this<br>condition is true, the flash() function is called with two arguments: the error<br>message &quot;Company name is required.&quot; and the alert category &quot;danger&quot;, which is likely<br>used to style the error message with a red color or some other<br>visual cue.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235030548-2573ac4a-cb7d-4f2f-b546-1e5675815486.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a code snippet that adds an error message to be displayed<br>if the address variable is empty or None.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235034543-3e2817ba-0a17-4369-8ada-8549a15cee6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a code snippet that adds an error message to be displayed<br>if the city variable is empty or None.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235213721-8d9ff2af-5883-4f4c-843c-5046f492323d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is a code snippet that adds an error message to be displayed<br>if the state variable is empty or None.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235214335-fec9ad31-2202-4fc7-b6f5-eb4d682e04bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here state is validated against pycountry package <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235214605-94b3037d-280b-4729-ac85-fd9f41e99f32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here code snippet shows that the country is required if not it shows<br>the flash error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235214876-052d05c8-b7ca-40cc-854c-ac4642847c8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here country is validated against pycountry package <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235215770-7457cd70-b3df-43d1-a291-c2c4cbc97174.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here code snippet shows that website can be choose or it can be<br>empty/none<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235216043-fe5cabc7-ec91-47e0-a6e8-6d2b2b3893fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here code snippet shows that the zipcode is required if not it shows<br>the flash error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235216239-1c67609c-54f2-4080-ada4-f19b4f6f2b68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code performs an SQL database insertion operation to add a new row<br>of company information into an IS601_MP3_Companies table, with columns for name, address, city,<br>country, state, zip, and website. The values to be inserted are passed as<br>arguments to the insertOne() method, which executes the SQL query with placeholder values<br>indicated by %s. The result variable likely stores the status or output of<br>the insertion operation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235217031-81c06018-600b-4bac-ae58-e423b7550ba2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code catches any exceptions that may occur during execution of the preceding<br>code block using a try-except block. If an exception occurs, it is stored<br>in the &#39;e&#39; variable and printed to the console using the print() statement.<br>Additionally, the code sets a message to be flashed on the webpage using<br>the Flask flash() function, indicating that an error occurred while adding the company<br>and prompting the user to try again. The &quot;danger&quot; parameter likely sets the<br>flash message to display with a red color or other warning indicator to<br>draw the user&#39;s attention to the error.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235217740-8526b84c-b255-4986-aeef-192e14338969.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>here the snippet shows the field in data for add company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235218009-4f0f3a6d-9dd4-4e20-9ff8-abcb01e84c74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet with data added and showing the success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235219178-67d7c7fe-75bc-4e56-bdd9-31ade551f562.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in the snippet it flashes an error message when name is not<br>entered<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235220195-2e1fb0d7-e8d1-4046-8eca-8c10bdea77a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in the snippet it flashes an error message when address is not<br>entered<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235220859-667ea247-01b3-4c01-8906-724614a2b719.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in the snippet it flashes an error message when city is not<br>entered<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235221441-d13eb9d9-e457-4d69-a481-2b287ee3240d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in the snippet it flashes an error message when state is not<br>entered<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235221932-e16a3169-3cac-4154-b249-e96683676fc6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in the snippet it flashes an error message when country is not<br>entered<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235222671-a88544f2-c5ee-4649-972a-2cc75766919a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in the snippet it flashes an error message when zip is not<br>entered<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235223548-ac506ae5-5c67-4eaa-909e-a62acbf92efe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the data which i added previously with UCID<br>and DB name is visible on the left side <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235224775-fc92a245-4215-4c69-be19-f92c353bd3f1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code creates an SQL query to retrieve information about companies and their<br>employees from two tables, IS601_MP3_Companies and IS601_MP3_Employees. The query selects columns for the<br>company&#39;s ID, name, address, city, country, state, zip code, website, and the count<br>of employees associated with the company. The SELECT statement uses a LEFT JOIN<br>to combine data from the two tables based on a matching company ID<br>in each table. The JOIN includes a subquery that counts the number of<br>employees associated with each company ID in the IS601_MP3_Employees table. The WHERE clause<br>includes a condition that is always true (1=1), which allows additional filtering conditions<br>to be appended to the query with the AND keyword.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235225429-d25b0c9c-63ca-4ec2-93c6-7b57aef5db5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code checks request args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235226828-b018a5c8-8ddd-4775-afdc-58467a01c47a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code appends a LIKE filter for name if provided with proper wildcards<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235227044-00c2fb51-0763-49a4-951a-3e7d1b4675ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code appends an equality filter for country if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235227235-c6af215e-7605-493b-b255-30b2beae20d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code appends an equality filter for state if provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235227386-87e41b6c-5a9c-458b-bac4-a219c2a33da5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code appends sorting if column and order are provided and within the<br>allows columns and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235227704-d9d28bd1-1fed-4e44-8958-966c014567ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code appends limit (default 10) or limit greater than or equal to<br>1 and less than or equal to 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235229610-aa369cbd-d2f2-4b09-adf1-2d204c3e43b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code provides a proper error message if limit isn&#39;t a number or<br>if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235229802-74f86630-ffc7-44fe-8196-4356a61c635e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This code has except block with a user friendly message flashed and a<br>print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235230550-2e17cac2-cc90-43a6-b9bc-e4df4edd8b8e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235231512-8e864de7-4812-4a4d-8ee1-4efac6191b28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235233382-ac4a1e08-f510-4efe-bd05-be5ac936023e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235232708-d829cf90-e00d-4ea5-95ae-29467454ba71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing one asc filter applied with id column chosen<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235232708-d829cf90-e00d-4ea5-95ae-29467454ba71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing one desc filter applied <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235234496-99c599c0-80e6-48c2-a7dd-c9fe012d4467.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is snippet of code which retrieves id (from request args) name, address,<br>city, state, country, zip, website from form. If id isn&#39;t present it flashes<br>error message and redirect to company search.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235234830-9acdccd4-298b-4d2e-a87d-b62dbe6d88ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is snippet where name is required , it flashes proper error message<br>if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235235053-50768b2f-ab7f-4e9a-b323-c9032776fa3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where address is required, it flashes proper error message<br>if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235235266-7e19e48c-9e93-4eaf-911a-4528894373d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where city is required, it flashes proper error message<br>if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235235563-488e8748-b240-47ad-ab27-aa0acc54fe2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where state is required, it flashes proper error message<br>if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235236038-5844c7c0-9d71-482c-887c-6e7bde7e6002.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where state is validated against pycountry package <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235236436-86541d0e-5a8a-4628-9963-ea87dd628646.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where country is required, it flashes proper error message<br>if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235236876-a28d6164-38f8-4a48-a769-b2c8c16d8ebc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet where country is validated against pycountry package <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235237169-7ddde1b3-4d38-41e6-8d4c-69e6988b1e55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet with proper UPDATE query and is visible with the<br>passed in data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235237475-7cafd80a-b24b-4ee6-8cbb-8fcef60e89c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for Except blocks (two) with a user friendly message<br>flashed and a print(e) of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235237747-2f5bacab-7770-40bf-8d26-765c2b1d8821.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for proper SELECT query and visible with the passed<br>in data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235238030-d19283c1-85e3-4cff-b210-826291739068.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for company data passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235238528-1684d3c1-e94e-406c-8c61-5b963b894c25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for data showing option to edit or delete <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235238901-eb053faa-fbfb-4bc9-ac10-f7e00cc0b7ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the data after editing. here i changed companies<br>name, website and zipcode<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235239077-87552549-7f22-419d-a58f-605879af3025.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the message that company record was updated <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235239381-e9b35d2a-a7a0-4c27-ac1f-d8c7dd9c3159.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the DB data before editing. I will be<br>editing id 4. UCID and DB name is visible on the left side<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235239858-71661623-f274-4a4a-95eb-1d362317f3f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the DB data after editing. Here in id<br>4 i edited company name, website and city. UCID and DB name is<br>visible on the left side <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235249254-c4e7cd37-5890-4d32-9190-fe8e5c4aba47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for Delete employee by id, if missing should flash<br>the related message, the it redirect to employee search, all request args (minus<br>id) are passed to the redirect route, success message is flashed when the<br>process worked <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235249462-1359f7ba-17ac-4f67-a5bf-6db2ccfd60e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the data of employee before deleting. i will<br>be deleting id 53.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235249562-2ebd927a-c623-4a79-b2da-7fdd48721060.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the data of employee after deleting and with<br>success message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235246985-9c305764-731b-40cd-bb7e-c7e7e59d7c12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for Delete company by id, if missing should flash<br>the related message, the it redirect to employee search, all request args (minus<br>id) are passed to the redirect route, success message is flashed when the<br>process worked <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235247858-0e2c7e1c-ed84-4320-9f03-44b400939ac6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the data of company before deleting. i will<br>be deleting id 2.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235248486-0c3bd52e-fa50-41d0-9568-397237c59ef1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the data of company after deleting and with<br>success message.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235250539-64a822c1-4630-4c71-b961-49edde7f8b83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for test case for add company with passing result<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235250884-f283078a-cae1-4551-8901-6549fa98d6c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for test case for add employee with passing result<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235251092-979a0c8f-5968-4bf8-ad3e-afe8bfd4b062.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for test case for edit company with passing result<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235251584-5a10c6ca-5f01-414f-9fb3-dc504e4225b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for test case for edit employee with passing result<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235251776-60b6efd6-719b-4eb2-bfde-eba8b8603063.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for test case for search company with passing result<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235251964-3c97b84b-03ca-475d-8d2e-e374f37f3bf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for test case for search employee with passing result<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/235252118-30dab168-4414-428d-87ac-e4a8a979858f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet for testing uplaod.csv<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I ran into many issues with code and also with heroku deployment. I<br>learned that small errors are the hardest part to fix n it takes<br>a long to find.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/rg695" target="_blank">Grading</a></td></tr></table>