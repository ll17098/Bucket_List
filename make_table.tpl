<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Bucket List</title>
</head>
<style>
body {
  backround-image: url("backriund for make table.jpg");
  background-repeat: no-repeat;
  background-attachment: fixed;

}
.nav {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}
li a {
  float: right;
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
.active {
  background-color: #1C4C83;
}
.field_wrap{
  text-align: center; 
}
th, td {
  border: 1px solid black;
  border-radius: 15px;
  padding: 15px;
  padding-bottom: 15px;
  padding-left: auto;
  padding-right: auto;
}
th {
  background-color: #1C4C83;
  color: white;
}
td {
  background-color: #7D8185;
  color: white;
  
}
.center { 
  margin-left: auto;
  margin-right: auto;
  width: 70%;
}
</style>
<body>
<div class="nav">
  <li style="float:left"><a class="active" href="index.html">Fill my Bucket</a></li>
  <li><a href="index.html">Home</a></li>
  <li><a href="logout.py">Log Out</a></li>
</div>


<div class="field_wrap">
  <h1>Here is your Bucket List</h1>
</div>

<table class="center">
<th>ID</th>
<th>Task</th>
<th>Status</th> 
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
<table>

</body>
</html>

