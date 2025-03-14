document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        window.location.href = document.querySelector('meta[name="redirect-url"]').content;
    }, 2000);
}); 