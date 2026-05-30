const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..', '..');
const srcFile = path.join(baseDir, 'skills_index.json');
const destDir = path.join(baseDir, 'apps', 'web-app', 'public');
const destFile = path.join(destDir, 'skills.json');

console.log('🔄 Setting up web application assets...');

if (!fs.existsSync(srcFile)) {
  console.error('❌ Error: skills_index.json not found in root directory! Run generate_index.py first.');
  process.exit(1);
}

if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

fs.copyFileSync(srcFile, destFile);
console.log(`✅ Mirrored skills database to: ${destFile}`);
