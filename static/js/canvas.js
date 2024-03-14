const ctx = canvas.getContext('2d');

// Fetch circle coordinates from the server
fetch('/circle-coordinates')
  .then(response => response.json())
  .then(data => {
    drawCircle(data.x, data.y, data.radius);
  })
  .catch(error => console.error('Error fetching circle coordinates:', error));

// Function to draw a circle
function drawCircle(x, y, radius) {
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, 2 * Math.PI);
  ctx.stroke();
}