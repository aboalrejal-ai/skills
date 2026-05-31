const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..', '..');
const webAppDir = path.join(rootDir, 'apps', 'web-app');

console.log('🔄 1. Preparing and mirroring skills database...');
try {
  execSync('npm run app:setup', { cwd: rootDir, stdio: 'inherit' });
} catch (error) {
  console.error('❌ Failed to run setup_web.js:', error.message);
  process.exit(1);
}

console.log('\n🚀 2. Deploying apps/web-app folder to gh-pages branch...');

// Force push method is the most reliable cross-platform (works on Windows/macOS/Linux)
// and handles uncommitted changes in the root repo perfectly without subtree requirements.
const tempGitDir = path.join(webAppDir, '.git');
if (fs.existsSync(tempGitDir)) {
  fs.rmSync(tempGitDir, { recursive: true, force: true });
}

try {
  // Get remote URL from the root repository
  const remoteUrl = execSync('git config --get remote.origin.url', { cwd: rootDir }).toString().trim();
  console.log(`🔗 Target Remote URL: ${remoteUrl}`);

  console.log('📦 Initializing temporary deployment repository...');
  execSync('git init', { cwd: webAppDir, stdio: 'ignore' });
  execSync('git add .', { cwd: webAppDir, stdio: 'ignore' });
  execSync('git commit -m "Deploy to GitHub Pages"', { cwd: webAppDir, stdio: 'ignore' });
  execSync(`git remote add origin ${remoteUrl}`, { cwd: webAppDir, stdio: 'ignore' });
  execSync('git checkout -b gh-pages', { cwd: webAppDir, stdio: 'ignore' });

  console.log('📤 Force pushing to remote gh-pages branch (this consumes ZERO GitHub Actions minutes)...');
  execSync('git push -u origin gh-pages --force', { cwd: webAppDir, stdio: 'inherit' });

  console.log('✨ Cleanup temporary git assets...');
  fs.rmSync(tempGitDir, { recursive: true, force: true });

  console.log('\n🎉 Successfully deployed! Your site will be live on GitHub Pages in a few moments.');
} catch (error) {
  console.error('\n❌ Deployment failed:', error.message);
  if (fs.existsSync(tempGitDir)) {
    fs.rmSync(tempGitDir, { recursive: true, force: true });
  }
  process.exit(1);
}
