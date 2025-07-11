document.addEventListener('DOMContentLoaded', () => {
  const flashDiv = document.getElementById('flash-messages');
  if (flashDiv) {
    setTimeout(() => {
      flashDiv.style.display = 'none';
    }, 4000); // 4 segundos
  }
});
