<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Vybhavi Chithapuram (vc435)</td></tr>
<tr><td> <em>Generated: </em> 4/19/2023 12:17:48 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/vc435" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232627885-428e331a-8de0-4ed3-89d0-343fc289d716.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output screeshot of passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232628184-4e350bcf-bf21-454c-9307-ffa52c6a76dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232628370-6869db16-007b-4e92-8a0f-125a4f85c955.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232628885-482571a0-8f25-41a6-a6f4-9189f2d9c193.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232629676-12cd9489-6eec-4537-8942-bd30320d6c14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232630009-ed308127-9b50-461d-94cf-88f9511c19bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232634735-4ab75bcf-d35c-44f3-9d26-21632f16454b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid user data from Task 1 should be present in this screenshot.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/15">https://github.com/vybhavi1212/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><div><div>1. We utilize WTforms to create and validate forms.</div><div>2. The accuracy of the<br>data entered into WTforms is checked both before and after submission.</div><div><br></div><div>Emails between 2<br>and 30 characters long that haven't been used by another user are verified<br>using an email validator.</div><div>3. Both the password and the confirm password need to<br>be eight words long and the same.</div><div>This is then checked with the help<br>of the wtform validators, hashed using the bcrypt hashing algorithm, and stored in<br>a database.</div><div>4. The hashed password, username, and email are kept in the users<br>table.</div><div><br></div><div><br></div></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232637262-b641de81-e3db-4199-81ad-9a8a162bbeae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232638400-fb253548-d80a-4be3-a5e7-5b9df4749a81.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232641118-aca515c9-4968-4f7f-a6fd-c17535143584.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/15">https://github.com/vybhavi1212/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>1.We will use the username or email field instead of the confirm password<br>field on the login form, which is handled using wt forms. In the<br>front end, if a username or email field has a "@," it will<br>use an email validator; otherwise, it will verify the username format, see if<br>the length is between 2 and 30 or not, and see if a<br>password has been provided or not. We get data from the users table<br>in the backend by giving the user's email and username. If we find<br>something, we compare the password and then decide whether the user has roles<br>assigned.</div><div><div>In the back end, we get the password from the database based on<br>the user name and email address and then check to see whether the<br>passwords match. whether they do, we remove the password from that point in<br>the program.</div><div>We get username, email, and password from the users database by passing<br>username and email, and then we check to see if the passwords match,<br>and then we look to see if the user has any roles assigned<br>from the user roles tables to find it.</div></div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232642073-8e1d4513-5720-411c-9a53-85ba8a76ca68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> successful logout message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232643702-806d4aa4-010b-4ce5-a4a4-dff77a8faa34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unauthorized access for logout user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/15">https://github.com/vybhavi1212/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>To work with and manage user sessions, we use the flask_login package.&nbsp;</div><div><br></div><div><div>Styled as<br>"font-family: Arial;"We'll use LoginManager in our main.py; tspan style="font-size: small; font-family: Arial;"&gt;this manages<br>our user session and offers practical tools.</div><div>We'll define a variable for login_manager outside<br>of the app factory since we're using one, and then inside the factory<br>we'll utilize its init_app() method to link the app.</div><div><br></div><div><br></div></div><div><div>The user_loader decorator will then<br>be used inside the app factory to execute a process to lookup a<br>user by id.</div><div><br></div><div><br></div></div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232643702-806d4aa4-010b-4ce5-a4a4-dff77a8faa34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unauthorized access for logout user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232645992-ef954ecf-aa3a-42fb-ae34-f7d91ef3c15a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>permission denied page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232646215-5d957df2-965f-428c-92f9-20511558c3e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>roles table with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232646955-3577b44a-407b-4515-91f0-506891f73d84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the only entry in userroles tables is my admin user(role id: -1) mapped<br>to the user with id: 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/15">https://github.com/vybhavi1212/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>In order to associate the app with the factory because we're using one,<br>we'll define a variable for login_manager outside of the factory.&nbsp;</div><div><br></div><div>The @login_required function is<br>used to adorn views for login-protected sites. If the user is not logged<br>in, the function calls the span class="pre" style="hyphens: none;"&gt; tag.unauthorized function in LoginManager.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>Here, we use the @admin_permission_require function from the roles.permissions package, similar to the<br>login protected page. We raise a 403 exception and display a 403 html<br>page with the message "Permission denied" if the user is not an administrator.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232653534-b4089951-b14f-4202-b945-d6d34028d429.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of navigation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232784277-904d2e7e-52e4-408b-ab58-551a2a9a7144.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>styled form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232882770-4a53dc12-4fd0-4e71-817f-2482ab18d4b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>good UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232885658-6eb5e1f6-3c9e-4fe0-a896-4201ff74d104.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB output display in a good manner<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/15">https://github.com/vybhavi1212/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>We utilize Bootstrap styling.&nbsp;</div><div><br></div><div>Navbars need to be wrapped.navbar featuring.navbar-expand-lg and bg-light are used<br>for responsive collapse at big break points and color, respectively.navbar-brand to represent the<br>project's name.navbar-nav provides full-height, lightweight navigation with dropdown support.</div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232884341-53fa50a8-579f-4509-92a6-9c14da6d17ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>login protected pages saying to the user &quot;unauthorized&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232884852-3f11de97-d5eb-4c27-a4d7-73e52bcd53dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>role protected pages saying to the user &quot;permission denied&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232885124-9258ef10-bd77-4257-a054-29755afde2dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email validation saying to the user that &quot;@ is not there and it<br>is not email&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/15">https://github.com/vybhavi1212/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>For 403 and 404 problems, we use flask error handler routines. In most<br>cases, we also look at what the backend code is doing and create<br>a flash message if a field is missing or something else is wrong.</div><div><br></div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232886095-882e68f3-30ba-4a3b-a2c2-7a7d9ca898f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>profile page with email and username prefilled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/15">https://github.com/vybhavi1212/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div>If a POST request is not sent when the profile page is accessed,<br>the email and username are retrieved from the users database using the user<br>id, and then they are rendered into the profile form.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232886472-aa679db2-9302-4af1-90bc-5e957c02251f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232888011-6cd42004-95c4-465b-9990-b77fd08112b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232888616-cf1eb287-7dbb-43d6-8a4b-47db67d606e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232891797-798d069b-2cbc-4679-8dad-edb81d71f396.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232897082-f00b622a-8aa5-45f4-8a3f-2800b900737a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> email/username already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232896577-2f09350f-93dc-4a8c-a818-d1518ab64526.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before profile edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/232896858-69796afb-bc95-4e5b-9ed2-7123c2139bc6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after profile edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/15">https://github.com/vybhavi1212/IS601-006/pull/15</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>The code first decides whether the request is a POST; if it is,<br>it then determines whether current_password, password, and confirm are provided; if they are,<br>it then retrieves the password from the users table; finally, the current password<br>and the password from the database are compared to determine whether they are<br>the same or not; if they are, an invalid password flask is raised;<br>otherwise, the new password is hashed and updated in the database.</div><div><br></div><div>A flash message<br>stating "saved profile" is then displayed after the username and email have been<br>updated in the database.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learned about how the flask roles work and also learned about the html<br>error files. Had some problems in heroku database but clarified them with the<br>help of the professor in office hours.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vc435-prod.herokuapp.com/login">https://is601-vc435-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/vc435" target="_blank">Grading</a></td></tr></table>