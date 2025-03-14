document.addEventListener('DOMContentLoaded', function() {
    document.body.addEventListener('htmx:configRequest', function(evt) {
        let token = document.querySelector('meta[name="csrf-token"]');
        if (token) {
            evt.detail.headers['X-CSRFToken'] = token.content;
        }
    });
}); 