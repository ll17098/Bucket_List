%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<link rel="stylesheet" type="text/css" href="/C:/Users/chunk/OneDrive/Desktop/Desktop Apps/Bucket_List/style.css" />

<p>Edit the task with ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
  <input type="text" name="task" value="{{old[0]}}">
  <select name="status">
    <option>open</option>
    <option>closed</option>
  </select>
  <br>
  <input type="submit" name="save" value="save">
  <form action="/todo" method="get">
  <button type="submit">Todo</button>
</form>