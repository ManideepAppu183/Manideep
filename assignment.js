const enrollStudentBtn = document.getElementById("enroll-student-btn");
const enrolledStudentsTable = document.createElement("table");

// Add table headers
const headers = ["Description", "Image"];
const headerRow = document.createElement("tr");
headers.forEach(header => {
  const th = document.createElement("th");
  th.textContent = header;
  th.style.backgroundColor = "#62a032";
  th.style.color = "#fff";
  th.style.border = "1px solid #62a032";
  headerRow.appendChild(th);
});

enrolledStudentsTable.appendChild(headerRow);

// Add h1 element
const enrolledStudentsTitle = document.createElement("h2");
enrolledStudentsTitle.textContent = "Enrolled Students";
enrolledStudentsTitle.style.color = "black"; 
enrolledStudentsTitle.style.backgroundColor = "#f2f2f2";
enrolledStudentsTitle.style.position = "absolute";
enrolledStudentsTitle.style.top = "70px";
enrolledStudentsTitle.style.right = "220px";
document.getElementById("enrolled-students").appendChild(enrolledStudentsTitle);

enrolledStudentsTable.style.borderCollapse = "collapse";
enrolledStudentsTable.style.border = "2px solid #62a032";
enrolledStudentsTable.style.width = "100%";

// Add borders between rows
const cells = enrolledStudentsTable.querySelectorAll("td, th");
cells.forEach(cell => {
  cell.style.borderBottom = "1px solid #ddd";
});

enrollStudentBtn.addEventListener("click", function(event) {
  event.preventDefault();

  // Get form values
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const website = document.getElementById("website").value;
  const imageLink = document.getElementById("image-link").value;
  const gender = document.querySelector('input[name="gender"]:checked').value;
  const skills = Array.from(document.querySelectorAll('input[name="skills"]:checked')).map(checkbox => checkbox.value).join(", ");

  const clearBtn = document.getElementById("clearBtn");
clearBtn.addEventListener("click", function(event) {
  event.preventDefault();
  document.getElementById("name").value = "";
  document.getElementById("email").value = "";
  document.getElementById("website").value = "";
  document.getElementById("image-link").value = "";
  document.querySelector('input[name="gender"]:checked').checked = false;
  document.querySelectorAll('input[name="skills"]:checked').forEach(checkbox => checkbox.checked = false);
});

  // Create new row
  const newRow = document.createElement("tr");
  const detailsCell = document.createElement("td");
  detailsCell.style.borderRight = "2px solid #62a032";
  detailsCell.innerHTML = `
    <p><strong>Name:</strong> ${name}</p>
    <p><strong>Gender:</strong> ${gender}</p>
    <p><strong>Email:</strong> ${email}</p>
    <p><strong>Website:</strong> <a href="${website}" target="_blank">${website}</a></p>

    <p><strong>Skills:</strong> ${skills}</p>
  `;
  newRow.appendChild(detailsCell);
  const imageCell = document.createElement("td");
  imageCell.style.borderLeft = "2px solid #62a032";
  imageCell.innerHTML = `<img src="${imageLink}" alt="${name}'s image" width="100">`;
  newRow.appendChild(imageCell);

  // Add row to table
  enrolledStudentsTable.appendChild(newRow);
  document.getElementById("enrolled-students").appendChild(enrolledStudentsTable);
});
