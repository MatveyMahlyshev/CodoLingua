let texts = document.querySelectorAll(".lang-description");
let maxLength = 740;
for (let textItem of texts) {
  if (textItem.textContent.length > maxLength) {
    let lastSpaceIndex = textItem.textContent.substring(0, maxLength).lastIndexOf(' ');
    if (lastSpaceIndex === -1) {
      lastSpaceIndex = maxLength;
    }
    textItem.textContent = textItem.textContent.substr(0, lastSpaceIndex) + "...";
  }
}