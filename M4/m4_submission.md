<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Rutva Gandhi (rg695)</td></tr>
<tr><td> <em>Generated: </em> 2/27/2023 10:52:54 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/rg695" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221685421-64fd0ee1-ce1b-40cf-ad65-6729a3d6d02d.png"/></td></tr>
<tr><td> <em>Caption:</em> <h1 id="ucid-rg695--date-02272023-summary-this-code-to-make-a-simplecalculator-using-functions-like-addition-selfans--num1num2-does-the-addition-and-totest-we-are-writing-test-cases-main-method-is-used-to-input-theequation-and-get-the-solution">UCID: RG695 # Date: 02/27/2023 #Summary: This code to make a simple<br>calculator using functions like addition. self.ans = num1+num2 does the addition. And to<br>test we are writing test cases. &quot;main&quot; method is used to input the<br>equation and get the solution.<br></h1>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221686623-492a8466-9737-4e90-a8c2-a41bf04756ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <h1 id="ucid-rg695--date-02272023-summary-this-code-to-make-a-simplecalculator-using-functions-like-subtraction-selfans--num1-num2-does-the-subtraction-and-totest-we-are-writing-test-cases-main-method-is-used-to-input-theequation-and-get-the-solution">UCID: RG695 # Date: 02/27/2023 #Summary: This code to make a simple<br>calculator using functions like subtraction. self.ans = num1-num2 does the subtraction. And to<br>test we are writing test cases. &quot;main&quot; method is used to input the<br>equation and get the solution.<br></h1>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221687046-1a40c7c2-af68-4319-981e-6754598b33c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <h1 id="ucid-rg695--date-02272023-summary-this-code-to-make-a-simplecalculator-using-functions-like-subtraction-selfans--num1num2-does-the-multiplication-and-totest-we-are-writing-test-cases-main-method-is-used-to-input-theequation-and-get-the-solution">UCID: RG695 # Date: 02/27/2023 #Summary: This code to make a simple<br>calculator using functions like subtraction. self.ans = num1*num2 does the multiplication. And to<br>test we are writing test cases. &quot;main&quot; method is used to input the<br>equation and get the solution.<br></h1>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221687252-dbc9d314-e84b-403b-aa22-461aafa7d3b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <h1 id="ucid-rg695--date-02272023-summary-this-code-to-make-a-simplecalculator-using-functions-like-subtraction-if-num2--0----printcant-divide-by-zero-sorry------else--selfans-num1num2-here-it-checks-for-the-num-entered-is-0-if-itis-0-it-gives-an-error-and-if-the-numbers-are-correct-itdivides-and-gives-the-answer-and-to-test-we-are-writing-test-casesmain-method-is-used-to-input-the-equation-and-get-the-solution">UCID: RG695 # Date: 02/27/2023 #Summary: This code to make a simple<br>calculator using functions like subtraction. if num2 == 0:    <br>print(&quot;Can&#39;t divide by zero, sorry&quot;)      else:  self.ans<br>= num1/num2 here it checks for the num entered is 0 if it<br>is 0 it gives an error and if the numbers are correct it<br>divides and gives the answer. And to test we are writing test cases.<br>&quot;main&quot; method is used to input the equation and get the solution.<br></h1>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221746321-653fa922-b530-427b-b6c0-b096c758b4ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the test case for adding 2 numbers is passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221746172-c6f983e3-d17e-4aea-86a9-c392c1b0c55a.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221747032-220c5a85-0e71-4a49-8bd0-86d53d7e6db2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Answer and a number is added.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221747208-2914c713-0cd1-4b49-83e6-f32428f7ea90.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221747421-1350a138-224f-4a32-8a70-9f40cf65112a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for subtraction of two numbers is passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221747554-3b600fe3-baa9-40c5-8ba9-439e756d49d4.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221747816-c87dedcb-9037-4aca-a9d9-da1471028243.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Answer and number is subtracted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221747932-6daf229e-1358-4e90-af35-e2ed3c72a0e3.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221748048-9448218b-f41e-46ea-9ff3-e1ea5ee6a012.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for multiplication is passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221748191-529ec8fb-2fd2-4b84-a107-2c5ec9aa00f1.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221748287-3852cfb2-23fe-4de3-8256-ef38c3e2f75a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for answer and a number is multiplied and passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221748491-c454e859-59e5-4dff-b8ae-fe6c0ba60c1c.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221748637-4c648b4b-e1f7-40a4-845f-b4d5a5092dfd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case for division of 2 numbers is passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221748889-85a9c23c-de29-4470-88bb-e3a8549698dd.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/221748974-e3776603-80c3-4df2-9131-e28b38c8fcf9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division for a answer and a number is done and tested<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>Learned to really test a code and faced some issues with test case<br>but tried and solved it.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Learned how to create a test case and also if it doesn&#39;t pass<br>how to fix them<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/rg695" target="_blank">Grading</a></td></tr></table>