<!-- search_results.php -->
<?php
// Connect to the database (you should have a separate connection file)
require('connect.php');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the search query
    $search = $_POST['search'];

    // Search for users
    $sql = "SELECT `id`, `username`, `email` FROM `users` WHERE `username` LIKE '%$search%' OR `email` LIKE '%$search%'";
    echo "$sql";
    $conn->multi_query($sql);
    $result = $conn->store_result();
    // NOTE: mysqli_multi_query allows us to simulate older methods of injection
    // mysql_query only allows for 1 SQL statement, preventing injection attacks to delete or drop from a select
    
    // Use of prepare can prevent hacks
    // $sql = "SELECT `id`, `username`, `email` FROM `users` WHERE `username` LIKE ? OR `email` LIKE ?";
    // $stmt = $conn->prepare($sql);
    // $searchvar="%".$search."%";
    // $stmt->bind_param("ss",$searchvar,$searchvar);
    // $stmt->execute();
    // $result = $stmt->get_result();

    if (mysqli_num_rows($result) > 0) {
        echo "<h2>Search Results:</h2>";
        echo "<table border='1'>";
        echo "<tr><th>ID</th><th>Username</th><th>Email</th></tr>";
        // while ($row = mysqli_fetch_assoc($result)) {
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>{$row['id']}</td><td>{$row['username']}</td><td>{$row['email']}</td>";
            echo "</tr>";
        }
        echo "</table>";
        echo "<p>&nbsp;</p>";
    } else {
        echo "No results found.";
    }

    // Close the database connection
    mysqli_close($conn);
}
?>

<!-- search_users.php -->
<form method="post" action="search_users.php">
    <input type="text" name="search" placeholder="Search users..." required>
    <input type="submit" value="Search"> &nbsp; 
    <button onClick='javascript:window.location="/"'>Home</button>
</form>
