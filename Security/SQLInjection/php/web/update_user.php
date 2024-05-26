<?php
// Include database connection file
require "connect.php";

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $id = $_GET['id'];
    $sql = "SELECT * FROM users WHERE id=$id";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            $username=$row['username'];
            $email=$row['email'];
        }
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (count($_POST) > 0) {
        $id = $_POST['id'];
        $username = $_POST['username'];
        $email = $_POST['email'];
        $password = $_POST['password'];

        // Don't change password if field is empty
        if ( isset($password) === TRUE and $password !== "" ) {
            $sql = "UPDATE users SET username='$username', email='$email', password=PASSWORD('$password') WHERE id=$id";
        } else {
            $sql = "UPDATE users SET username='$username', email='$email' WHERE id=$id";
        }

        if (mysqli_query($conn, $sql)) {
            echo "Record updated successfully";
        } else {
            echo "Error updating record: " . mysqli_error($conn);
        }
    }
    echo '<script type="text/JavaScript">setTimeout("location.href = \'/list_users.php\';",0);</script>"';
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Update User</title>
    <link rel="stylesheet" href="core.css">
</head>
<body>
    <h1>Update User</h1>
    <form method="post" action="update_user.php">
        <input type='hidden' name='id' value="<?php echo $_GET['id'] ?>">
    <table border="1">
        <?php if ( isset($username) === TRUE ): ?>
            <tr><td>Username:</td><td><input type="text" name="username" value="<?php echo $username ?>" required></td></tr>
        <?php else: ?>
            <tr><td>Username:</td><td><input type="text" name="username" required></td></tr>
        <?php endif ?>
        <?php if (isset($email) === TRUE): ?>
            <tr><td>Email:</td><td><input type="email" name="email" value="<?php echo $email ?>" required></td></tr>
        <?php else: ?>
            <tr><td>Email:</td><td><input type="email" name="email" required></td></tr>
        <?php endif ?>
        <tr><td>Password:</td><td><input type="password" name="password"></td></tr>
        <tr><td colspan='2' align='center'><button type="submit">Update User</button> &nbsp; <button onClick='javascript:window.location="/"'>Home</button></td></tr>
    </table>
    </form>
</body>
</html>


