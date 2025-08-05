function slowreaction() {
    let username = document.getElementById("username").value;
    const unre = /^\w+ \w+$/;
    let skip = true;

    if ( unre.test(username) ) {
        alert("Username is acceptable");
    } else {
        alert("Username is WRONG!");
        skip = false;
        // Don't submit the form due to errors
        return false;
    }

    if ( skip ) {
        result = confirm("Are you sure this is correct "+username+"?");
    }
    return true;
}

document.getElementById("email").value = "steve@neueda.com";