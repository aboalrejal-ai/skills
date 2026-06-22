const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const match = html.match(/<style>([\s\S]*?)<\/style>/);
if (match) {
  fs.mkdirSync('src/styles', { recursive: true });
  fs.writeFileSync('src/styles/globals.css', match[1].trim());
  console.log("CSS extracted successfully.");
} else {
  console.log("CSS not found.");
}
