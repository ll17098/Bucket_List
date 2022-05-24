<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Bucket List</title>
</head>
<style>
html {
  backround-image: url("mtbackr.jpg");
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
li a, .dropdown {
  float: right;
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
li a:hover {
  background-color: #7D8185;
}
.active {
  background-color: #1C4C83;
}
.dropdown {
  position: relative;
  display: inline-block;
}
.dropbtn {
  background-color: #1C4C83;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}
.dropdown-content {
  display: none;
  position: absolute;
  background-color: white;
  min-width: 170px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  text-align: center;
}

.dropdown-content a {
  display: block;
  width: 1
  color: black;
  padding: 16px;
  text-decoration: none;
  
}

.dropdown-content a:hover {background-color: #7D8185}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: #1C4C83;
}

.container {
  margin-top: 100px;
  margin-bottom: auto;
}

.field_wrap {
  margin-left: auto;
  margin-right; auto;
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
.tbl { 
  margin-left: auto;
  margin-right: auto;
  width: 70%;
}

</style>



<body>
<div class="nav">
  <li style="float:left"><a class="active" href="index.html">Fill my Bucket</a></li>
  <li><a href="logout.py">Log Out</a></li>
  <li><a href="index.html">Home</a></li>
</div>

<div class="dropdown">
  <button class="dropbtn">Bucket List Options</button>
  <div class="dropdown-content">
    <a href="/edit">Edit Current Item</a>
    <a href="/new">Add new Item</a>
  </div>
</div>


<div class="container">
  <div class="field_wrap">
    <h1>Here is your Bucket List</h1>
  </div>
  <table class="tbl">
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
</div>

</body>
</html>

