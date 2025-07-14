document.addEventListener('DOMContentLoaded', () => {
  // Hide flash messages after 4 seconds
  const flashDiv = document.getElementById('flash-messages');
  if (flashDiv) {
    setTimeout(() => {
      flashDiv.style.display = 'none';
    }, 4000); // 4 secs
  }
});
