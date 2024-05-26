<?php
$host = "database";
$username = "root";
$password = "secret123";
$dbname = "user_accounts";

// Create connection
$conn = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
