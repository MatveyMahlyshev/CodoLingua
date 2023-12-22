document.addEventListener('DOMContentLoaded', function () {
    var paragraphs = document.getElementsByTagName('p');

    for (var i = 0; i < paragraphs.length; i++) {
        var paragraph = paragraphs[i];

        var text = paragraph.textContent;

        if (text.trim().endsWith('Пример ниже:')) {
            var divElement = document.createElement('div');
            divElement.classList.add('code-example');

            var preElement = document.createElement('pre');
            var codeElement = document.createElement('code');
            var headerElement = document.createElement('header');
            var spanPython = document.createElement('span');
            var spanCopy = document.createElement('span');
            var buttonElement = document.createElement('button');

            spanPython.textContent = 'python';

            buttonElement.textContent = 'copy';

            codeElement.innerHTML = '{{code.code1}}'

            spanCopy.appendChild(buttonElement);
            headerElement.appendChild(spanPython);
            headerElement.appendChild(spanCopy);

            preElement.appendChild(codeElement);
            divElement.appendChild(preElement);
            divElement.appendChild(headerElement);

            paragraph.insertAdjacentElement('afterend', divElement);

        }
    }
});