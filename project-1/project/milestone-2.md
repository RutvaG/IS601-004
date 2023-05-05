<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Vybhavi Chithapuram (vc435)</td></tr>
<tr><td> <em>Generated: </em> 4/28/2023 6:32:32 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/vc435" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/234713302-11f1fb17-3333-4f30-842b-2c57bd2dfc61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin create page with a valid data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/234713656-3b044727-bfbc-42f6-8ba0-ad01c1a43ef4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing all the products and the latest added product is highlighted in<br>the last(fish)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;">As soon as the values are input on<br>the add page, they are delivered to the item function in shop.py. It<br>checks to verify if an id has been passed before deciding whether the<br>action is to modify or add. Here is</span></font></div><div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI,<br>Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;"><br></span></font></div><div><font<br>color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji,<br>Segoe UI Emoji"><span style="font-size: 16px;">No id is provided, so an INSERT statement is<br>executed transferring the values to the Products table, and if successful, a flash<br>is displayed. Since no id is supplied, a create action is required.</span></font></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vc435-prod.herokuapp.com/admin/items">https://is601-vc435-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/234724109-3d7a3079-ce6a-4b10-8c3b-dc8737b3d7df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot of the Shop page showing items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/234725248-bebe44ae-0808-4f05-ba68-207ddd25d354.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Shop page showing both filter with food and sorted from<br>low to high price<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/234726466-d486e27d-1aef-46b4-a5d0-1baa57afcebd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the filter/sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <div><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;">The Products table, whose visibility is set to<br>1, provides the initial data for the shop page. The page also offers<br>name searches, category choices, and "High to Low" or "Low to High" sorting<br>of prices. when we carry out a search using one or more of<br>the aforementioned methods. Then, based on the input, we modify the where condition<br>of the query in the shop list of the shop.py function.</span></font></div><div><font color="#1f2328" face="-apple-system,<br>BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI<br>Emoji"><span style="font-size: 16px;">then display the results once more.</span></font></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vc435-prod.herokuapp.com/shop?name=&category=Electronics&price=ASC">https://is601-vc435-prod.herokuapp.com/shop?name=&category=Electronics&price=ASC</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235147763-0f9eff99-f156-48f6-a6f5-bb5d4397c6e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Admin List page/results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div dir="auto" style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;,<br>&quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;<br>background-color: rgb(246, 248, 250);"><div dir="auto" style="box-sizing: border-box;">We select every field from the Products<br>database and feed it directly into the HTML page without using any filters.</div><div<br>dir="auto" style="box-sizing: border-box;">No conditions are mentioned, so every product will be displayed regardless<br>of visibility.</div><div><br></div></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vc435-prod.herokuapp.com/admin/items">https://is601-vc435-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235147953-eff372c6-139a-4829-b44a-5ee1acbd26bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Shop<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235148121-fa6a894d-0ca8-446a-8c54-682307ea152a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235148286-5e16caf3-8879-47c3-8378-f0f68c06bc19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add a screenshot showing the edit button visible to the Admin on the<br>Admin Product List Page (The admin page)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235154046-4e36af0d-c83c-4cb4-b4e4-dc4bcd62f23a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the list of products after editing the product Tesla..123<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235153577-29529ecd-f4b6-4c93-80be-7765ea721012.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the list of products before editing the product Tesla<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235153787-c8c2f368-38d3-4de6-898f-4771ff96c2a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit page with changed details of the product Tesla..123<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div dir="auto" style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;,<br>&quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;<br>background-color: rgb(246, 248, 250);"><div dir="auto" style="box-sizing: border-box;">In shop.html, each product contains a check<br>to determine if the user is signed in and if they are an<br>administrator. If all conditions are met, we show a button for editing the<br>item, which directs the user to the page with the item's specifications.</div><div dir="auto"<br>style="box-sizing: border-box;">If the user is an admin, the edit button is shown on<br>the item details page.</div><div dir="auto" style="box-sizing: border-box;">The edit button is the default on<br>the admin items page because only administrators can access it.</div></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vc435-prod.herokuapp.com/admin/item?id=24">https://is601-vc435-prod.herokuapp.com/admin/item?id=24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235160662-260bcccb-1bdc-4b5a-9e71-6e20f6d91ac1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the button (clickable item) that directs the user to the Product<br>Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235161791-1cbcb550-151d-4220-ab88-c07b30947b61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the result of the Product donut  Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div dir="auto" style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;,<br>&quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;<br>background-color: rgb(246, 248, 250);"><div dir="auto" style="box-sizing: border-box;">I created the itemdetails.html and item details<br>routines just for this.</div><div dir="auto" style="box-sizing: border-box;">Clicking the product name will send the<br>product id to the item details function, which will use the id to<br>extract all the data from the Products database and show it on the<br>item details page.</div></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vc435-prod.herokuapp.com/admin/item?id=23">https://is601-vc435-prod.herokuapp.com/admin/item?id=23</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235164155-31929fcb-612a-45b0-a830-0956d8ccf17a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding  donut to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235164505-2d254ca8-e8f1-40d5-a5cc-c77b1362a8fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the error message of adding to cart when not logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235165320-be470de5-f2cd-4376-90dd-bbf9ce7e0e4d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p dir="auto" style="box-sizing: border-box; background-color: rgb(246, 248, 250);"><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI,<br>Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">I<br>created the itemdetails.html and item details routines just for this.</span></font></p><p dir="auto" style="box-sizing: border-box;<br>background-color: rgb(246, 248, 250);"><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial,<br>sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">Clicking the product name will<br>send the product id to the item details function, which will use the<br>id to extract all the data from the Products database and show it<br>on the item details page.</span></font></p><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI, Noto Sans, Helvetica, Arial, sans-serif, Apple Color<br>Emoji, Segoe UI Emoji"><span style="font-size: 16px;">The product id is supplied as a hidden<br>field to the cart function in shop.py when the ADD button is clicked.<br>As long as the quantity is greater than 0, we then enter the<br>product id, user id, desired quantity, and unit pricing (fetching it from the<br>products table).</span></font><br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235167512-9eea2569-6433-4d4c-9039-3b0c65db0ba9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View with subtotal of each line and adding up,<br>cart total, link to product details page for each product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <div dir="auto" style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;,<br>&quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;<br>background-color: rgb(246, 248, 250);"><div dir="auto" style="box-sizing: border-box;">If a product id is not supplied<br>when we click the cart, the method detects that this is not an<br>add or update function and tries to see if one is being passed<br>instead. The next step is to navigate to the SELECT block where it<br>retrieves the user and product identifiers, name, and requested quantity. It then calculates<br>the subtotal by dividing the quantity you want by the unit price and<br>sends these values to cart.html.</div><div dir="auto" style="box-sizing: border-box;">The subtotal value for each row<br>is added to a variable named ns.total, and the total is then displayed<br>at the bottom. Each item is rendered as a row in a table<br>in the HTML output for the purpose of computing the total.</div></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vc435-prod.herokuapp.com/cart">https://is601-vc435-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235168160-e904426a-4c88-43db-9fcd-8d33c9b39e1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing before updating the quantity of product hm<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235168650-c34486dc-a683-428c-b52f-c807a9917285.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing after updating the quantity of product hm to 4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235169424-84ef3ce4-e159-4bc1-bda3-3fecabd0d1fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing of cart before setting the quantity to 0 for product hm<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235169750-09453f6e-acdc-4de2-b60f-2f0d51e39c42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing of cart after setting the quantity to 0 for product hm<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235170060-9514cc33-25da-466d-bf75-8f91577dd8a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing how a negative quantity is handled when tried to set -1 to<br>fish<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div dir="auto" style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;,<br>&quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;<br>background-color: rgb(246, 248, 250);"><div dir="auto" style="box-sizing: border-box;">- A hidden product id is given<br>to the cart function when we click the update button next to the<br>amount field and update button in the cart.</div><div dir="auto" style="box-sizing: border-box;">- The code<br>retrieves the name and price from the products table if the quantity is<br>more than 0, then updates the quantity and price in the cart table<br>while providing the product id and user id.</div><div dir="auto" style="box-sizing: border-box;">- When we<br>enter 0 in the amount box, the code advances to the DELETE block<br>where we delete the product from the cart database while giving the product<br>id and user id because the number is less than 0.</div><div dir="auto" style="box-sizing:<br>border-box;">- To accommodate negative amounts in the input field's minimum value in HTML,<br>we set it to 0.</div></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235171384-fc7abc52-00f7-4454-851d-ed7f1ff588e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the cart before deleting the product donut<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235172071-e907ba2e-df34-4b69-a79b-bdd7b57b0c59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the cart after deleting the product Sony ZV-1F vlog camera from<br>the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235172287-a8f32321-ac2f-4df8-9209-275b243e9ff2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing before clearing a cart completely<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/235172674-4416ccf8-94a6-4751-a302-b8ce93818bf9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing after the clearing the cart completely<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div dir="auto" style="box-sizing: border-box; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;,<br>&quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;<br>background-color: rgb(246, 248, 250);"><div dir="auto" style="box-sizing: border-box;">A hidden field amount of -1 will<br>be provided next to the delete button when a single item is removed<br>from a cart. If the hidden field amount is less than zero, the<br>cart function will perform the delete query while delivering the product id.</div><div dir="auto"<br>style="box-sizing: border-box;">If the value of the delete all variable in the cart method<br>is True, we delete the records in the Cart table while passing the<br>user id. This is done to erase the entire cart.</div></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/16">https://github.com/vybhavi1212/IS601-006/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p dir="auto" style="box-sizing: border-box; background-color: rgb(246, 248, 250);"><font color="#1f2328" face="-apple-system, BlinkMacSystemFont, Segoe UI,<br>Noto Sans, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">One<br>of the places where I ran into trouble was when I was creating<br>the tables because the cart table depends on the product table and the<br>query to create the cart table comes before creating the product table, so<br>even though my product table was already created, the items were unable to<br>be added to the cart. When I realized this, I ran inti_db.py once<br>more, and the cart table was created.</span></font></p><p dir="auto" style="box-sizing: border-box; background-color: rgb(246, 248,<br>250);"><span style="font-size: 16px; color: rgb(31, 35, 40); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto<br>Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;">The rest was all<br>routine, and I had the chance to learn how to create websites for<br>a real-world project.</span><br></p><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-vc435-prod.herokuapp.com/login">https://is601-vc435-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/vc435" target="_blank">Grading</a></td></tr></table>