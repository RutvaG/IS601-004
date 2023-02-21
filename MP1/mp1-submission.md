<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Rutva Gandhi (rg695)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 11:10:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/rg695" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/219966871-d8e2de70-aa7f-43df-bc4f-152118f70b03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The &#39;add_task&#39; function takes in a task name, description, and due date, creates<br>a new task object based on the task template, sets its properties with<br>the provided data, and adds it to the tasks list. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220229278-7257b62d-88d3-41a2-af53-b3ab38c88917.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it rejects the task due to invalid string<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220229779-f8ef96f8-ed77-42b1-9ab0-2091026be180.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it prints the success message when task added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p><span style="color: rgb(22, 25, 43); font-family: &quot;Haas Grot Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica,<br>arial, sans-serif; font-size: 15px;">The &#39;add_task&#39; function takes in a task name, description, and<br>due date, creates a new task object based on the task template, sets<br>its properties with the provided data, and adds it to the tasks list.&nbsp;</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220230799-6b8e0645-005f-4095-844f-c0bf84a92b3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this function edits the task we want to update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>this function edits the task which needs to be updated and ask the<br>description of the task which needs to be updated<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220230799-6b8e0645-005f-4095-844f-c0bf84a92b3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asks for index and finds the task associated with that index and updates<br>it when information is added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220230799-6b8e0645-005f-4095-844f-c0bf84a92b3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shows if the task was updated or not<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p><span style="color: rgb(22, 25, 43); font-family: &quot;Haas Grot Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica,<br>arial, sans-serif; font-size: 15px;">The &#39;update_task&#39; function updates an existing task&#39;s properties based on<br>the provided index and updated task data.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220233176-fa9e2581-8ccb-4e2c-9077-784bdef9d71f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The &#39;mark_done&#39; function marks a task as done by setting its completion status<br>to the current datetime.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220233176-fa9e2581-8ccb-4e2c-9077-784bdef9d71f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this function checks if the task has been completed or not<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p><span style="color: rgb(22, 25, 43); font-family: &quot;Haas Grot Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica,<br>arial, sans-serif; font-size: 15px;">The mark_done function updates a single task, identified by index,<br>to a done status by recording the current datetime as the completion time.&nbsp;</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220238621-8e0fdd5a-fc5d-4dd5-9ba2-938ef3270e65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this function helps us to view the task by index<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> <p>got and error while doing this task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220238974-85962179-e083-445d-a27a-83c52f0b60d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> The delete function removes a task from the tasks list by index<br>and prints the message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220238974-85962179-e083-445d-a27a-83c52f0b60d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>here it shows if the task which we asked to delete was deleted<br>or not<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p><span style="color: rgb(22, 25, 43); font-family: &quot;Haas Grot Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica,<br>arial, sans-serif; font-size: 15px;">&nbsp;The delete function removes a task from the tasks list<br>by index. it uses len to get the index.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220242260-5e23e739-5249-4ec8-8ab4-88896c271657.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it displays the task which has to be completed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220242260-5e23e739-5249-4ec8-8ab4-88896c271657.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shows 3 incomplete tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220243055-ee9b06a2-5cf4-4002-9b9f-db9961fc9171.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this shows the list of incomplete task and the done tasks are marked<br>with x<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>this shows the list of incomplete tasks and the done tasks are marked<br>with x<div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220243876-9ed8a9f3-2800-4cc4-a1d6-ec207396322e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the task with the due date missed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220243876-9ed8a9f3-2800-4cc4-a1d6-ec207396322e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success shows 1 over due task <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>it shows the tasks that are overdue it uses the list_task function to<br>display the overdue task.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220244548-a21e36c1-0325-4701-960e-e7c3f3f54402.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows if the task is pending or overdue with the duration of<br>time<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220244548-a21e36c1-0325-4701-960e-e7c3f3f54402.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows how many days,hours,minutes, seconds until due<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>outputs the number of days, hours, minutes, seconds a task has before its<br>overdue date<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220245236-52687953-22b3-40c0-af03-e45b054d9e28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the list of task with the detail<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113145/220245385-426023e4-a840-47b8-a804-05f65b3e3f2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>this shows the help command which will display the choices of command again<br>and quit is used to exit <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p style="box-sizing: border-box; --tw-ring-color:rgba(59,130,246,0.5); --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1;<br>--tw-scroll-snap-strictness:proximity; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0<br>0 #0000; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure:<br>; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-blur: ; --tw-brightness: ; --tw-contrast: ;<br>--tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur:<br>; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ;<br>--tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 0px; color: rgb(22, 25, 43); font-family: &quot;Haas Grot<br>Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica, arial, sans-serif; font-size: 15px;">The code defines several functions<br>that work together to create a simple task tracker application. The tasks list<br>holds the tasks that have been added to the system. The TASK_TEMPLATE constant<br>is a template that provides the structure of a task, with the name,<br>due date, last activity date, description, and completion status of a task.</p><p style="box-sizing:<br>border-box; --tw-ring-color:rgba(59,130,246,0.5); --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-scroll-snap-strictness:proximity; --tw-ring-offset-width:0px;<br>--tw-ring-offset-color:#fff; --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000;<br>--tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing:<br>; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ;<br>--tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness:<br>; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ;<br>--tw-backdrop-sepia: ; margin-bottom: 0px; color: rgb(22, 25, 43); font-family: &quot;Haas Grot Text Web&quot;,<br>&quot;Helvetica Neue&quot;, helvetica, arial, sans-serif; font-size: 15px;">&nbsp;</p><p style="box-sizing: border-box; --tw-ring-color:rgba(59,130,246,0.5); --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0;<br>--tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-scroll-snap-strictness:proximity; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0<br>0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom:<br>; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ;<br>--tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate:<br>; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ;<br>--tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 0px; color:<br>rgb(22, 25, 43); font-family: &quot;Haas Grot Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica, arial, sans-serif;<br>font-size: 15px;">The str_to_datetime function converts a string in either of two formats into<br>a datetime object that can be stored in the task tracker. The save<br>function writes the contents of the tasks list to a JSON file to<br>persist changes, and the load function reads the tasks from the JSON file.<br>The list_tasks function lists a summary of all tasks in the tasks list.</p><p<br>style="box-sizing: border-box; --tw-ring-color:rgba(59,130,246,0.5); --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-scroll-snap-strictness:proximity;<br>--tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0<br>#0000; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ;<br>--tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale:<br>; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ;<br>--tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate:<br>; --tw-backdrop-sepia: ; margin-bottom: 0px; color: rgb(22, 25, 43); font-family: &quot;Haas Grot Text<br>Web&quot;, &quot;Helvetica Neue&quot;, helvetica, arial, sans-serif; font-size: 15px;">&nbsp;</p><p style="box-sizing: border-box; --tw-ring-color:rgba(59,130,246,0.5); --tw-border-spacing-x:0; --tw-border-spacing-y:0;<br>--tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-scroll-snap-strictness:proximity; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-offset-shadow:0 0 #0000;<br>--tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-pan-x: ; --tw-pan-y: ;<br>--tw-pinch-zoom: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset:<br>; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ;<br>--tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale:<br>; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 0px;<br>color: rgb(22, 25, 43); font-family: &quot;Haas Grot Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica, arial,<br>sans-serif; font-size: 15px;">The add_task function takes in the name, description, and due date<br>of a task and adds it to the tasks list by copying the<br>TASK_TEMPLATE and filling in the data provided. The process_update function prompts the user<br>for the data for a task and passes the data to the update_task<br>function, which updates the name, description, and due date of a task found<br>by index if the data was provided.</p><p style="box-sizing: border-box; --tw-ring-color:rgba(59,130,246,0.5); --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0;<br>--tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-scroll-snap-strictness:proximity; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0<br>0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom:<br>; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ;<br>--tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate:<br>; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ;<br>--tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 0px; color:<br>rgb(22, 25, 43); font-family: &quot;Haas Grot Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica, arial, sans-serif;<br>font-size: 15px;">&nbsp;</p><p style="box-sizing: border-box; --tw-ring-color:rgba(59,130,246,0.5); --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1;<br>--tw-scale-y:1; --tw-scroll-snap-strictness:proximity; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000;<br>--tw-shadow-colored:0 0 #0000; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-ordinal: ; --tw-slashed-zero: ;<br>--tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-blur: ; --tw-brightness: ; --tw-contrast:<br>; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ;<br>--tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity:<br>; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 0px; color: rgb(22, 25, 43); font-family: &quot;Haas<br>Grot Text Web&quot;, &quot;Helvetica Neue&quot;, helvetica, arial, sans-serif; font-size: 15px;">The mark_done function updates<br>a single task, identified by index, to a done status by recording the<br>current datetime as the completion time. The delete function removes a task from<br>the tasks list by index. The main function is the main entry point<br>of the application, which presents the user with a menu of options to<br>add, update, mark done, delete, or list tasks.</p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/rg695" target="_blank">Grading</a></td></tr></table>
