var jsonData = {
    "trainers": [
        {
            "name": "Steve",
            "age": 30,
            "subjects": ["JavaScript", "HTML", "CSS", "Python", "Java"]
        },
        {
            "name": "Chrstine",
            "age": 28,
            "subjects": ["React", "Node.js", "Express", "MongoDB"]
        },
        {
            "name": "Nick",
            "age": 26,
            "subjects": ["Java", "Spring", "Hibernate", "SQL"]
        }
    ]
}

function fillTable() {
    var table = document.getElementById("trainersTable");
    
    // Heading
    var headerRow = table.createTHead().insertRow();
    headerRow.style = "background-color:rgb(255, 154, 154); text-align: center; font-size: 18pt; font-weight: bolder;";
    var nameHeader = headerRow.insertCell(0);
    nameHeader.textContent = "Trainer Name";
    nameHeader.style.padding = "10px";
    var subjectsHeader = headerRow.insertCell(1);
    subjectsHeader.textContent = "Subjects";


    let trainers = JSON.stringify(jsonData.trainers);
    jsonData.trainers.forEach(function(trainer) {
        var row = table.insertRow();
        row.style = "text-align: center; font-size: 14pt;";
        var nameCell = row.insertCell(0);
        nameCell.style.padding = "2px";
        var subjectsCell = row.insertCell(1);
        subjectsCell.style.padding = "2px";

        nameCell.textContent = trainer.name;
        subjectsCell.textContent = trainer.subjects.join(", ");
    });
}