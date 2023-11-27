// Получаем список элементов с классом 'subtopics'
let subtopicsParent = document.querySelector('.subtopics-list')
let subtopics = document.querySelectorAll('.subtopics');
let aside = document.querySelector('aside');

// Перебираем каждый элемент списка
subtopics.forEach(function(subtopic) {
    // Разделяем содержимое элемента на массив подстрок
    let parts = subtopic.textContent.split(', ');

    // Перебираем каждую подстроку
    parts.forEach(function(part) {
        // Создаем новый элемент div
        let newDiv = document.createElement("li");
        let newButton = document.createElement('button');

        newDiv.classList.add('subtopic');

        // Записываем в него содержимое до ", "
        newDiv.textContent = part.charAt(0).toUpperCase() + part.slice(1);;

        // Добавляем новый div в текущую HTML-страницу
        subtopicsParent.appendChild(newDiv);
    });

});
subtopics.forEach(function(subtopic) {
    // Удаляем элемент
    subtopic.remove();
});