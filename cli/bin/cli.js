#!/usr/bin/env node

/**
 * aboalrejal-skills CLI
 * Interactive zero-dependency CLI to browse, search, and install AI agent skills across 20+ platforms.
 * 
 * Design Philosophy:
 * - 100% Zero External Dependencies (instantly runnable via `npx`).
 * - Beautiful ANSI colored text and fully interactive menu using raw stdout/stdin.
 * - Dynamic registry loading (locally or remotely from GitHub).
 */

import fs from 'fs';
import path from 'path';
import https from 'https';
import readline from 'readline';
import { fileURLToPath } from 'url';

// --- STYLING & COLORS (ANSI) ---
const C = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  dim: '\x1b[2m',
  underscore: '\x1b[4m',
  blink: '\x1b[5m',
  reverse: '\x1b[7m',
  hidden: '\x1b[8m',
  
  black: '\x1b[30m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
  white: '\x1b[37m',
  gray: '\x1b[90m',
  
  bgBlack: '\x1b[40m',
  bgRed: '\x1b[41m',
  bgGreen: '\x1b[42m',
  bgYellow: '\x1b[43m',
  bgBlue: '\x1b[44m',
  bgMagenta: '\x1b[45m',
  bgCyan: '\x1b[46m',
  bgWhite: '\x1b[47m'
};

const BANNER = `
${C.cyan}${C.bright} █████╗ ██████╗  ██████╗  █████╗ ██╗     ██████╗ ███████╗     ██╗ █████╗ ██╗     
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║     ██╔══██╗██╔════╝     ██║██╔══██╗██║     
███████║██████╔╝██║   ██║███████║██║     ██████╔╝█████╗        ██║███████║██║     
██╔══██║██╔══██╗██║   ██║██╔══██║██║     ██╔══██╗██╔══╝   ██   ██║██╔══██║██║     
██║  ██║██████╔╝╚██████╔╝██║  ██║███████╗██║  ██║███████╗╚█████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚════╝ ╚═╝  ╚═╝╚══════╝${C.reset}
            ${C.yellow}${C.bright}🌟 THE ULTIMATE UNIFIED AI AGENT SKILLS HUB 🌟${C.reset}
`;

// Remote URL to download registry.json and skill markdown files
const GITHUB_REPO_OWNER = 'aboalrejal-ai';
const GITHUB_REPO_NAME = 'skills';
const GITHUB_BRANCH = 'main';
const REMOTE_REGISTRY_URL = `https://raw.githubusercontent.com/${GITHUB_REPO_OWNER}/${GITHUB_REPO_NAME}/${GITHUB_BRANCH}/docs/skills-registry.json`;
const REMOTE_RAW_BASE = `https://raw.githubusercontent.com/${GITHUB_REPO_OWNER}/${GITHUB_REPO_NAME}/${GITHUB_BRANCH}/`;

// --- REGISTRY AND DATA LOADING ---
let cachedRegistry = null;

async function fetchURL(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'aboalrejal-skills-cli' } }, (res) => {
      if (res.statusCode !== 200) {
        reject(new Error(`Failed to load: ${res.statusCode} ${res.statusMessage}`));
        return;
      }
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

async function loadRegistry() {
  if (cachedRegistry) return cachedRegistry;

  // 1. Try local file first (for development)
  const __dirname = path.dirname(fileURLToPath(import.meta.url));
  const localPaths = [
    path.join(__dirname, '..', 'docs', 'skills-registry.json'),
    path.join(__dirname, '..', '..', 'docs', 'skills-registry.json')
  ];

  for (const localPath of localPaths) {
    if (fs.existsSync(localPath)) {
      try {
        const raw = fs.readFileSync(localPath, 'utf8');
        cachedRegistry = JSON.parse(raw);
        return cachedRegistry;
      } catch (err) {
        // Fallback to fetch
      }
    }
  }

  // 2. Fetch remotely
  process.stdout.write(`${C.cyan}🔄 Fetching online skills registry...${C.reset}\n`);
  try {
    const raw = await fetchURL(REMOTE_REGISTRY_URL);
    cachedRegistry = JSON.parse(raw);
    return cachedRegistry;
  } catch (err) {
    console.error(`${C.red}❌ Error fetching skills registry: ${err.message}${C.reset}`);
    process.exit(1);
  }
}

// --- INTERACTIVE SELECT MENU CORE ---
function cleanScreen() {
  process.stdout.write('\u001b[2J\u001b[0;0H');
}

/**
 * Renders an interactive scrollable selection list
 */
function interactiveSelect(title, options, callback) {
  let selectedIndex = 0;
  const stdin = process.stdin;
  const stdout = process.stdout;
  
  stdin.setRawMode(true);
  stdin.resume();
  stdin.setEncoding('utf8');

  function draw() {
    // Clear screen and reset cursor
    cleanScreen();
    stdout.write(BANNER);
    stdout.write(`\n${C.bright}${C.yellow}👉 ${title}${C.reset}\n\n`);

    options.forEach((opt, idx) => {
      const label = typeof opt === 'string' ? opt : opt.label;
      const desc = opt.desc ? ` - ${C.gray}${opt.desc}${C.reset}` : '';
      if (idx === selectedIndex) {
        stdout.write(`  ${C.cyan}${C.bright}➔ [ ${label} ]${C.reset}${desc}\n`);
      } else {
        stdout.write(`     ${label}${desc}\n`);
      }
    });

    stdout.write(`\n${C.dim}Use [↑/↓ Arrow Keys] to navigate, [Enter] to select, [Ctrl+C] to exit.${C.reset}\n`);
  }

  function onKey(key) {
    if (key === '\u0003') { // Ctrl+C
      cleanup();
      process.exit(0);
    }
    if (key === '\r' || key === '\n') { // Enter
      cleanup();
      callback(options[selectedIndex], selectedIndex);
      return;
    }
    if (key === '\u001b[A') { // Up arrow
      selectedIndex = (selectedIndex - 1 + options.length) % options.length;
      draw();
    }
    if (key === '\u001b[B') { // Down arrow
      selectedIndex = (selectedIndex + 1) % options.length;
      draw();
    }
  }

  function cleanup() {
    stdin.removeListener('data', onKey);
    stdin.setRawMode(false);
    stdin.pause();
  }

  draw();
  stdin.on('data', onKey);
}

// --- LIST OF PLATFORMS ---
const PLATFORMS = [
  { id: 'antigravity', label: 'Google Antigravity', desc: 'Saves directly to Antigravity user plugins directory' },
  { id: 'claude-win', label: 'Claude Code (Windows)', desc: 'Saves to local .claudecode skill folder' },
  { id: 'claude-unix', label: 'Claude Code (Linux/Mac)', desc: 'Saves to local .claudecode skill folder' },
  { id: 'cursor', label: 'Cursor IDE', desc: 'Adds custom rules inside .cursor/rules/' },
  { id: 'devin', label: 'Devin CLI', desc: 'Adds instructions inside .devin/instructions/' },
  { id: 'aider', label: 'Aider AI', desc: 'Saves as .aider.instruction.<name>.md at project root' },
  { id: 'copilot-cli', label: 'GitHub Copilot CLI', desc: 'Saves configuration under .github/copilot-instructions.md' },
  { id: 'copilot-vscode', label: 'VS Code Copilot Chat', desc: 'Saves inside .github/copilot-instructions.md' },
  { id: 'trae', label: 'Trae', desc: 'Saves in project instructions directory' },
  { id: 'trae-cn', label: 'Trae CN', desc: 'Saves in project instructions directory' },
  { id: 'gemini-cli', label: 'Gemini CLI', desc: 'Saves in local gemini config folder' },
  { id: 'codex', label: 'Codex', desc: 'Saves in local root workspace directory' },
  { id: 'opencode', label: 'OpenCode', desc: 'Saves in root workspace directory' },
  { id: 'claw', label: 'OpenClaw', desc: 'Saves to claw-instructions/' },
  { id: 'droid', label: 'Factory Droid', desc: 'Saves to droid-skills/' },
  { id: 'hermes', label: 'Hermes', desc: 'Saves to local project instructions' },
  { id: 'kimi', label: 'Kimi Code', desc: 'Saves to kimi-instructions/' },
  { id: 'amp', label: 'Amp', desc: 'Saves to amp-rules/' },
  { id: 'kiro', label: 'Kiro IDE/CLI', desc: 'Saves to kiro-instructions/' },
  { id: 'pi', label: 'Pi coding agent', desc: 'Saves in local project workspace' },
  { id: 'cwd', label: 'Custom Workspace Directory (CWD)', desc: 'Saves directly to current active directory' }
];

// --- FLOWS ---

async function mainMenu() {
  const reg = await loadRegistry();
  interactiveSelect(
    `Welcome! We have ${C.cyan}${reg.total_skills}${C.yellow} active skills online. What would you like to do?`,
    [
      { label: '🔍 Search Skills', action: runSearch },
      { label: '📂 Browse by Category', action: browseCategories },
      { label: '📜 List All Skills', action: listAllSkills },
      { label: '🚪 Exit', action: () => process.exit(0) }
    ],
    (selected) => {
      selected.action();
    }
  );
}

function runSearch() {
  cleanScreen();
  console.log(BANNER);
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.question(`\n${C.bright}${C.cyan}🔎 Enter search keyword (e.g. "seo", "fullstack", "art"): ${C.reset}`, async (query) => {
    rl.close();
    const reg = await loadRegistry();
    const cleanQuery = query.toLowerCase().trim();
    
    if (!cleanQuery) {
      console.log(`${C.yellow}⚠️ Search query cannot be empty.${C.reset}`);
      setTimeout(mainMenu, 1500);
      return;
    }

    const matches = reg.skills.filter(s => 
      s.name.toLowerCase().includes(cleanQuery) || 
      s.description.toLowerCase().includes(cleanQuery) ||
      s.category.toLowerCase().includes(cleanQuery)
    );

    if (matches.length === 0) {
      console.log(`\n${C.red}❌ No skills found matching "${query}".${C.reset}`);
      rl.question(`\nPress Enter to return to main menu...`, () => mainMenu());
      return;
    }

    const options = matches.map(s => ({
      label: s.name,
      desc: s.description,
      skill: s
    }));
    options.push({ label: '🔙 Back to Main Menu', skill: null });

    interactiveSelect(
      `Found ${matches.length} matching skills. Select one to install:`,
      options,
      (selected) => {
        if (!selected.skill) {
          mainMenu();
        } else {
          startInstallationFlow(selected.skill);
        }
      }
    );
  });
}

function browseCategories() {
  loadRegistry().then(reg => {
    const options = reg.categories.map(cat => ({
      label: cat.replace(/-/g, ' ').toUpperCase(),
      catName: cat
    }));
    options.push({ label: '🔙 Back to Main Menu', catName: null });

    interactiveSelect(
      'Choose a Category to explore:',
      options,
      (selected) => {
        if (!selected.catName) {
          mainMenu();
        } else {
          const categorySkills = reg.skills.filter(s => s.category === selected.catName);
          const skillOptions = categorySkills.map(s => ({
            label: s.name,
            desc: s.description,
            skill: s
          }));
          skillOptions.push({ label: '🔙 Back to Categories', skill: null });

          interactiveSelect(
            `Skills under ${selected.label} (${categorySkills.length} total):`,
            skillOptions,
            (selectedSkill) => {
              if (!selectedSkill.skill) {
                browseCategories();
              } else {
                startInstallationFlow(selectedSkill.skill);
              }
            }
          );
        }
      }
    );
  });
}

function listAllSkills() {
  loadRegistry().then(reg => {
    const options = reg.skills.map(s => ({
      label: s.name,
      desc: `[${s.category}] ${s.description}`,
      skill: s
    }));
    options.push({ label: '🔙 Back to Main Menu', skill: null });

    interactiveSelect(
      'Listing all available skills. Select one to install:',
      options,
      (selected) => {
        if (!selected.skill) {
          mainMenu();
        } else {
          startInstallationFlow(selected.skill);
        }
      }
    );
  });
}

// --- INSTALLATION LOGIC ---

function startInstallationFlow(skill) {
  interactiveSelect(
    `Installing "${skill.name}". Select your target platform:`,
    PLATFORMS,
    async (platform) => {
      cleanScreen();
      console.log(BANNER);
      console.log(`\n${C.cyan}📦 Resolving installation path for ${C.bright}${platform.label}${C.reset}...`);

      const cwd = process.cwd();
      let targetPath = '';

      switch (platform.id) {
        case 'antigravity':
          // Locate User AppData or Home Directory for Antigravity
          const home = process.env.USERPROFILE || process.env.HOME || cwd;
          targetPath = path.join(home, '.gemini', 'config', 'plugins', 'aboalrejal-skills', 'skills', skill.category, skill.name, 'SKILL.md');
          break;
        case 'claude-win':
        case 'claude-unix':
          targetPath = path.join(cwd, '.claudecode', 'skills', skill.category, skill.name, 'SKILL.md');
          break;
        case 'cursor':
          targetPath = path.join(cwd, '.cursor', 'rules', `${skill.name}.md`);
          break;
        case 'devin':
          targetPath = path.join(cwd, '.devin', 'instructions', `${skill.name}.md`);
          break;
        case 'aider':
          targetPath = path.join(cwd, `.aider.instruction.${skill.name}.md`);
          break;
        case 'copilot-cli':
        case 'copilot-vscode':
          targetPath = path.join(cwd, '.github', 'copilot-instructions.md');
          break;
        case 'trae':
        case 'trae-cn':
          targetPath = path.join(cwd, '.instructions', `${skill.name}.md`);
          break;
        case 'gemini-cli':
          targetPath = path.join(cwd, '.gemini', 'skills', `${skill.name}.md`);
          break;
        case 'claw':
          targetPath = path.join(cwd, 'claw-instructions', `${skill.name}.md`);
          break;
        case 'droid':
          targetPath = path.join(cwd, 'droid-skills', `${skill.name}.md`);
          break;
        case 'kimi':
          targetPath = path.join(cwd, 'kimi-instructions', `${skill.name}.md`);
          break;
        case 'amp':
          targetPath = path.join(cwd, 'amp-rules', `${skill.name}.md`);
          break;
        case 'kiro':
          targetPath = path.join(cwd, 'kiro-instructions', `${skill.name}.md`);
          break;
        default:
          targetPath = path.join(cwd, 'skills', skill.category, skill.name, 'SKILL.md');
          break;
      }

      console.log(`${C.gray}📁 Destination: ${targetPath}${C.reset}`);

      // Fetch Skill Content
      const remoteSkillURL = `${REMOTE_RAW_BASE}${skill.path}`;
      process.stdout.write(`${C.cyan}📥 Fetching skill contents from remote repository...${C.reset}\n`);

      try {
        let content = '';
        
        // Optimize offline flow if local workspace exists
        const __dirname = path.dirname(fileURLToPath(import.meta.url));
        const localSkillFile = path.resolve(__dirname, '..', skill.path);
        
        if (fs.existsSync(localSkillFile)) {
          content = fs.readFileSync(localSkillFile, 'utf8');
        } else {
          content = await fetchURL(remoteSkillURL);
        }

        // Write the file
        fs.mkdirSync(path.dirname(targetPath), { recursive: true });

        // If it's a shared instruction file (like Copilot instructions), append to it safely
        if (platform.id === 'copilot-cli' || platform.id === 'copilot-vscode') {
          let existing = '';
          if (fs.existsSync(targetPath)) {
            existing = fs.readFileSync(targetPath, 'utf8') + '\n\n';
          }
          fs.writeFileSync(targetPath, `${existing}# Skill: ${skill.name}\n${content}`, 'utf8');
        } else {
          fs.writeFileSync(targetPath, content, 'utf8');
        }

        console.log(`\n${C.green}${C.bright}🎉 SUCCESS! Skill "${skill.name}" has been installed perfectly.${C.reset}`);
        console.log(`${C.gray}Path: ${targetPath}${C.reset}\n`);

      } catch (err) {
        console.error(`\n${C.red}❌ Error installing skill: ${err.message}${C.reset}`);
      }

      const rl2 = readline.createInterface({
        input: process.stdin,
        output: process.stdout
      });
      rl2.question(`Press Enter to return to main menu...`, () => {
        rl2.close();
        mainMenu();
      });
    }
  );
}

// --- CLI ENTRY ---

async function run() {
  const args = process.argv.slice(2);
  const reg = await loadRegistry();

  if (args.length > 0) {
    const cmd = args[0].toLowerCase();
    
    if (cmd === 'list') {
      console.log(`${C.bright}${C.yellow}📜 ALL AVAILABLE SKILLS (${reg.total_skills}):${C.reset}\n`);
      reg.skills.forEach(s => {
        console.log(`- ${C.cyan}${C.bright}${s.name}${C.reset} (${C.dim}${s.category}${C.reset}): ${s.description}`);
      });
      process.exit(0);
    }
    
    if (cmd === 'search') {
      const keyword = args.slice(1).join(' ').toLowerCase();
      if (!keyword) {
        console.error(`${C.red}❌ Please provide a search term. Example: aboalrejal-skills search seo${C.reset}`);
        process.exit(1);
      }
      const matches = reg.skills.filter(s => 
        s.name.toLowerCase().includes(keyword) || 
        s.description.toLowerCase().includes(keyword)
      );
      console.log(`${C.bright}${C.yellow}🔍 SEARCH RESULTS FOR "${keyword}" (${matches.length} matches):${C.reset}\n`);
      matches.forEach(s => {
        console.log(`- ${C.cyan}${C.bright}${s.name}${C.reset} (${C.dim}${s.category}${C.reset}): ${s.description}`);
      });
      process.exit(0);
    }

    if (cmd === 'install') {
      const skillName = args[1];
      if (!skillName) {
        console.error(`${C.red}❌ Please provide a skill name. Example: aboalrejal-skills install page-cro${C.reset}`);
        process.exit(1);
      }
      const skill = reg.skills.find(s => s.name.toLowerCase() === skillName.toLowerCase());
      if (!skill) {
        console.error(`${C.red}❌ Skill "${skillName}" not found in registry.${C.reset}`);
        process.exit(1);
      }
      startInstallationFlow(skill);
      return;
    }

    console.log(`${C.red}❌ Unknown command: ${args[0]}${C.reset}`);
    console.log(`Usage:\n  npx aboalrejal-skills [list | search <query> | install <skill-name>]`);
    process.exit(1);
  }

  // Run interactive GUI
  mainMenu();
}

run();
