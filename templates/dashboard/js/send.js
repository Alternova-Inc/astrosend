document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('files');
    const fileList = document.querySelector('.file-list');
    const fileListItems = document.querySelector('.file-list-items');
    const fileListTotal = document.querySelector('.file-list-total');
    const maxSize = parseInt(fileInput.dataset.maxSize);
    let currentFiles = [];

    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    function updateFileList() {
        const newFiles = Array.from(fileInput.files);
        currentFiles = [...currentFiles, ...newFiles];
        
        if (currentFiles.length > 0) {
            fileList.style.display = 'block';
            let totalSize = 0;
            fileListItems.innerHTML = '';
            
            currentFiles.forEach(file => {
                totalSize += file.size;
                const fileItem = document.createElement('div');
                fileItem.className = 'file-item';
                fileItem.textContent = `${file.name} (${formatFileSize(file.size)})`;
                fileListItems.appendChild(fileItem);
            });
            
            fileListTotal.textContent = `Total: ${formatFileSize(totalSize)}`;
            
            if (totalSize > maxSize) {
                fileListTotal.classList.add('error');
                fileListTotal.textContent = `Total size exceeds 50MB limit: ${formatFileSize(totalSize)}`;
            } else {
                fileListTotal.classList.remove('error');
            }
        } else {
            fileList.style.display = 'none';
            fileListTotal.textContent = '';
        }
    }

    fileInput.addEventListener('change', updateFileList);
}); 