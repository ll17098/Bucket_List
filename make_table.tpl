<link rel="stylesheet" type="text/css" href="/C:/Users/chunk/OneDrive/Desktop/Desktop Apps/Bucket_List/style.css" />
<p>The open items are as follows:</p>
<table border="1">
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
</table>
<style>
th, td {
  border: 1px solid black;
  border-radius: 10px;
}
</style>