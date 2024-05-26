<?php
// Include your database connection configuration (e.g., connect.php)
require('connect.php');

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve user input (sanitize and validate as needed)
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Hash the password (use a secure hashing algorithm, e.g., bcrypt)
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Insert the user data into the database
    $sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sss", $username, $email, $hashedPassword);

    if ($stmt->execute()) {
        echo "User added successfully!";
    } else {
        echo "Error adding user: " . $stmt->error;
    }

    // Close the database connection
    $stmt->close();
    $conn->close();

    echo '<script type="text/JavaScript">setTimeout("location.href = \'/list_users.php\';",1500);</script>"';
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Add User</title>
    <link rel="stylesheet" href="core.css">
</head>
<body>
    <h1>Add User</h1>
    <form method="post" action="add_user.php">
    <table border="1">
        <tr><td>Username:</td><td><input type="text" name="username" required></td></tr>
        <tr><td>Email:</td><td><input type="email" name="email" required></td></tr>
        <tr><td>Password:</td><td><input type="password" name="password" required></td></tr>
        <tr><td colspan='2' align='center'><button type="submit">Add User</button> &nbsp; <button onClick='javascript:window.location="/"'>Home</button></td></tr>
    </table>
    </form>
</body>
</html>
