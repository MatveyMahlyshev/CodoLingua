let paragraphs = document.querySelectorAll("p");

paragraphs.forEach(function (paragraph, index) {
  if (paragraph.textContent.includes("Заголовок:")) {
    let newHeader = document.createElement("h2");
    let newId = index;
    newHeader.id = newId;
    newHeader.textContent = paragraph.textContent.replace("Заголовок:", "");
    paragraph.replaceWith(newHeader);
  } else if (paragraph.textContent.includes("Подзаголовок:")) {
    let newSubHeader = document.createElement("h3");
    newSubHeader.textContent = paragraph.textContent.replace(
      "Подзаголовок:",
      ""
    );
    paragraph.replaceWith(newSubHeader);
  }
});