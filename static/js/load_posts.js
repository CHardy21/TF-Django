let offset = 4;

document.getElementById('load-more').addEventListener('click', () => {
    fetch(`/posts/load_posts/?offset=${offset}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('post-container')
                .insertAdjacentHTML('beforeend', data.html);

            offset += 4;

            if (!data.quedan_posts) {
                document.getElementById('load-more').style.display = 'none';
            }
        })
        .catch(error => console.error('Error al cargar más posts:', error));
});
