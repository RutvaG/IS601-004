<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Rutva Gandhi (rg695)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 5:00:28 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/rg695" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236544992-e417bc43-616a-4d73-822d-0f1dec257736.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing admin creating item page with a valid data<br>in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236546881-72ed5057-49ba-45d6-bcd0-6ee79ff1db26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing all the products and the latest added product<br>is at the last which is turkey<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>When the user enters values on the &quot;add&quot; page, these values are immediately<br>passed to the &quot;item&quot; function in the &quot;shop.py&quot; file. The function checks whether<br>an ID has been provided, and based on that, decides whether to modify<br>an existing record or create a new one. In this case, since no<br>ID has been provided, the function executes an &quot;INSERT&quot; statement to transfer the<br>values to the &quot;Products&quot; table. If the insertion is successful, a message is<br>displayed to indicate that the operation was successful. This means that a new<br>record has been created.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rg695-prod.herokuapp.com/admin/item">https://is601-rg695-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236550062-f0e218d1-e570-4a9e-a530-ba4d701e270d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the 8 sample items showing heroku dev url<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236550264-5f50a5dd-4d4d-4a5b-aa14-da1451e7b201.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here are the other 2 sample so total of 10 <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236550572-e7c7197e-18c1-429e-bea2-841b293eacfb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the Shop page which shows both filter with<br>food and sorted from low to high price<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236551089-a47a8293-a966-4eee-95e6-6c9f5b813e97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the filter/sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p style="border: 0px solid rgb(217, 217, 227); box-sizing: border-box; --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0;<br>--tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-gradient-from-position:<br>; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ;<br>--tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0 0 transparent; --tw-ring-shadow:0 0 transparent;<br>--tw-shadow:0 0 transparent; --tw-shadow-colored:0 0 transparent; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale:<br>; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ;<br>--tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate:<br>; --tw-backdrop-sepia: ; margin-top: 1.25em; margin-bottom: 1.25em;">The filters are applied to the SQL<br>query by appending the relevant conditions to the query string. If the name&nbsp;parameter<br>is present, the query string will include a condition that filters by the<br>name&nbsp;column. If the category&nbsp;parameter is present, the query string will include a condition<br>that filters by the category&nbsp;column. If the price&nbsp;parameter is present, the query string<br>will include an ORDER BY&nbsp;clause that sorts the results by the unit_price&nbsp;column in<br>ascending or descending order based on the value of the price parameter. The<br>resulting SQL query is executed, and the resulting rows are displayed on the<br>shop.html&nbsp;template. If there are no rows that match the filter criteria, no products<br>will be displayed.</p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rg695-prod.herokuapp.com/shop?name=&category=Food&price=DESC">https://is601-rg695-prod.herokuapp.com/shop?name=&category=Food&price=DESC</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236553435-5a879114-0513-4c2f-aeae-254bddb33af5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing admin list page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>This code retrieves all the fields from the &quot;Products&quot; database table and displays<br>them on the HTML page without applying any filters. Since no filter conditions<br>are specified, all the products in the table will be displayed regardless of<br>their visibility.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rg695-prod.herokuapp.com/admin/items">https://is601-rg695-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236554433-f1e882f0-4df1-4c68-80f0-c9ccc01821e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the edit button visible to the Admin on<br>the shop page with visible heroku dev url<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236554820-37e5459f-2673-4645-8fe1-54d7ab526e79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the edit button visible to the Admin on<br>the product details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236555042-db552fef-3685-4fae-8132-73335832e23b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the edit button visible to the Admin on<br>the Admin Product List Page (The admin page) <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236555511-d63b7834-69fc-4674-b617-94ef36d65272.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the product editing page before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236555878-12bb565b-a563-4b27-a1a9-6b40352f3393.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the product editing page after editing it from<br>cheese to chia pudding<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p style="border: 0px solid rgb(217, 217, 227); box-sizing: border-box; --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0;<br>--tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-gradient-from-position:<br>; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ;<br>--tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0 0 transparent; --tw-ring-shadow:0 0 transparent;<br>--tw-shadow:0 0 transparent; --tw-shadow-colored:0 0 transparent; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale:<br>; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ;<br>--tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate:<br>; --tw-backdrop-sepia: ; margin-bottom: 1.25em;">The shop.html&nbsp;template contains a check for whether the user<br>is logged in and whether they are an administrator. If both conditions are<br>met, an "Edit" button is displayed for each product on the page, which<br>directs the user to a page where they can modify the product's details.<br>On the item details page, the "Edit" button is displayed only if the<br>logged-in user is an administrator. By default, on the administrator items page, the<br>"Edit" button is displayed for all products because only administrators have access to<br>it.</p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rg695-prod.herokuapp.com/admin/item?id=5">https://is601-rg695-prod.herokuapp.com/admin/item?id=5</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236561069-2c836bbd-3458-4bd0-ac06-e91877e733be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing  the button (clickable item) that directs the<br>user to the Product Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236561249-e126c440-f752-4820-b2ce-a39ab5c9359f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the result of the product details page when<br>clicked on Bed sheets<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>To display the details of a particular product, the itemsdetails.html&nbsp;template and item_detail()&nbsp;function were<br>created. When the user clicks on the name of a product, the product<br>ID is sent to the item_detail()&nbsp;function as a parameter. The function then uses<br>the ID to extract all the data from the "Products" database table for<br>that particular product and displays it on the itemdetails.html&nbsp;page. This allows the user<br>to view all the details of the product on a separate page.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rg695-prod.herokuapp.com/itemdetails?id=-4">https://is601-rg695-prod.herokuapp.com/itemdetails?id=-4</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236562087-a51ef92b-9c37-46ef-b151-39cfa4dfcdec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the success message of adding Healthy chocolate to<br>cart <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236562451-09e52c6f-4f7f-4795-9ba8-7fbf7ce23ace.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the error message of adding to cart when<br>user not logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236562797-98fca62e-c12d-42eb-a522-b817ea4a6ef0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>The itemdetails.html&nbsp;template and item_details()&nbsp;function were specifically created to display the details of a<br>particular product. When a user clicks on the name of a product, the<br>product ID is passed to the item_details()&nbsp;&nbsp;function as an argument. The function then<br>uses this ID to retrieve all the information about the product from the<br>&quot;Products&quot; database table and displays it on the&nbsp;&nbsp;itemdetails.html&nbsp;page. In summary, the&nbsp;&nbsp;itemdetails.html&nbsp;template and item_details()&nbsp;&nbsp;function<br>are used to show all the details of a product when the user<br>clicks on its name.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>When the user clicks on the &quot;ADD&quot; button to add a product to<br>the cart, the product ID is passed as a hidden field to the<br>cart()&nbsp;function in shop.py(). If the quantity entered is greater than 0, the function<br>then inserts the product ID, user ID, desired quantity, and unit pricing (retrieved<br>from the &quot;Products&quot; table) into the cart table. In summary, the cart()&nbsp;function adds<br>a product to the cart by inserting its details into the cart table,<br>including the product ID, user ID, desired quantity, and unit pricing.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236563995-44c94183-e1b0-4b2d-bed5-1c9cc5ff2cd6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of the Cart View with subtotal of each line<br>and adding up, cart total, link to product details page for each product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>If a product ID is not supplied when the &quot;Cart&quot; button is clicked,<br>the function in shop.py&nbsp;checks if it is an add or update function. If<br>it is not, then it goes to a SELECT block where it retrieves<br>the user and product identifiers, name, and requested quantity from the cart table.<br>The function then calculates the subtotal for each item by dividing the quantity<br>requested by the unit price and passes these values to cart.html. Each item<br>is displayed as a row in a table in the HTML output, and<br>the subtotal value for each row is added to a variable. Finally, the<br>total of all subtotals is displayed at the bottom of the table. In<br>summary, the cart()&nbsp;function retrieves items from the cart table, calculates the subtotal for<br>each item, and displays them as rows in a table on the cart.html<br>page. It also computes the total of all subtotals and displays it at<br>the bottom of the table.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rg695-prod.herokuapp.com/cart">https://is601-rg695-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236564744-2feb2f7c-abbf-46c2-b2c9-277c60eb989f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of cart quantity update before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236565121-413a73e0-d732-4115-8d80-0a7a9e5c5a6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of cart quantity to 2 update after editing and<br>also it updates the total<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236565626-b265be09-52c0-448f-bb0d-88281c6d1bf1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing the before of the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236565804-76646b3d-e012-42c6-b680-3592350985de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet showing cart after when quantity set to 0 <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236566058-ef402749-d4b9-4842-94a4-db51317a1710.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of how the negative quantity is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>When the update button next to the quantity field is clicked, the cart<br>function receives a hidden product id. If the quantity entered is greater than<br>0, the function retrieves the name and price of the product from the<br>products table and updates the quantity and price in the cart table, using<br>the product id and user id. If the quantity entered is 0 or<br>less, the function moves to the DELETE block, where it deletes the product<br>from the cart table, using the product id and user id. To allow<br>for negative quantities in the quantity field, the minimum value in the HTML<br>input field is set to 0.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236566565-7579c5f4-2791-4622-a638-f51596a988d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of before deleting a single item from the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236566774-2d922670-60f2-4b27-9c9f-34cf6b2053ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of after deleting a single item from the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236566900-397c8099-dd5f-454f-8022-370abf79ad67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of before clearing the cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/236567026-47487675-2e85-4cbd-8782-7171a5c446b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here is the snippet of after when cart is cleared<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>When a user removes a single item from their cart, a hidden field<br>with a value of -1 will be generated alongside the delete button. If<br>the value of the hidden field is less than zero, the cart function<br>will initiate a delete query, passing the product id as a parameter. If<br>the delete all variable in the cart method is set to True, all<br>records in the Cart table for the specified user will be deleted, effectively<br>erasing the entire cart.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985">https://github.com/RutvaG/IS601-004/pull/42#issue-1698047985</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>During the process of creating tables for the website, an issue arose due<br>to the dependency of the cart table on the product table. The query<br>to create the cart table was executed before creating the product table, which<br>caused items to be unable to be added to the cart, despite the<br>product table already being created. Upon recognizing this problem, the init_db.py script was<br>rerun, resulting in the successful creation of the cart table. After resolving this<br>issue, the rest of the process became standard, and it provided a valuable<br>learning experience for developing websites for a practical project.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rg695-prod.herokuapp.com/login">https://is601-rg695-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/rg695" target="_blank">Grading</a></td></tr></table>