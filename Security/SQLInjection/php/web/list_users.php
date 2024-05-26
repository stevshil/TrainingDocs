<?php
// Database connection parameters
require('connect.php');

// Query to retrieve user accounts
$sql = "SELECT id, username, email FROM users";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html>
<head>
    <title>User Accounts</title>
    <link rel="stylesheet" href="core.css">
</head>
<body>
    <h1>User Accounts</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
        </tr>
        <?php
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td><a href='/update_user.php?id=".$row['id']."'>" . $row['id'] . "</a></td>";
                echo "<td>" . $row['username'] . "</td>";
                echo "<td>" . $row['email'] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<tr><td colspan='3'>No records found.</td></tr>";
        }
        ?>
        <tr><td colspan="3" align='center'><button onClick='javascript:window.location="/"'>Home</button></td></tr>
        <tr><td colspan="3" align='center'>Click the ID to modify a user</td></tr>
    </table>
</body>
</html>

<?php
// Close the database connection
$conn->close();
?>
