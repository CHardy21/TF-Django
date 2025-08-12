document.addEventListener('DOMContentLoaded', function () {
    const input = document.querySelector('input[type="file"]');
    if (!input) return;

    const preview = document.createElement('img');
    preview.id = 'preview-imagen';
    preview.style.maxHeight = '300px';
    preview.style.marginTop = '10px';
    preview.classList.add('img-fluid');

    // Mostrar imagen actual si existe
    const initialUrl = input.dataset.initial || input.getAttribute('data-initial');
    if (initialUrl) {
        preview.src = initialUrl;
        preview.style.display = 'block';
    }

    input.parentNode.appendChild(preview);

    input.addEventListener('change', function () {
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.onload = function (e) {
                preview.src = e.target.result;
                preview.style.display = 'block';
            };
            reader.readAsDataURL(input.files[0]);
        } else {
            preview.src = '#';
            preview.style.display = 'none';
        }
    });
});
