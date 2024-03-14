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
  ctx.strokeStyle = "rgb(0, 0, 0)";
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, 2 * Math.PI);
  ctx.stroke();
}

ctx.font = "48px serif";
ctx.fillText("Hello world", 10, 50);

datalista = [0,2, 0.5, 0.8, 0.3]

start_x = 300
start_y = 200
width = 300
height = 100

ctx.beginPath();
// y-axis
ctx.lineTo(start_x, start_y);
ctx.lineTo(start_x, start_y + height);
// x-axis
ctx.moveTo(start_x, start_y + height)
ctx.lineTo(start_x, start_y + height);
ctx.lineTo(start_x + width, start_y + height);

ctx.stroke();



