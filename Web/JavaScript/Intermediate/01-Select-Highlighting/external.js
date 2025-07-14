function highlightCountry(country) {
    
    let counter = 0;
    document.querySelectorAll('td').forEach(td => {
        if (td.textContent === country) {
            counter = 1;
            td.classList.add('highlight');
        } else {
            if ( counter > 0 && counter < 3 ) {
                td.classList.add('highlight');
                counter++;
            } else {
                td.classList.remove('highlight');
                counter=0;
            }
        }
    });
}