#!/usr/bin/env node

'use strict';

const { spawn, spawnSync } = require('node:child_process');
const path = require('node:path');
const fs = require('node:fs');

const args = process.argv.slice(2);
const PYTHON_ENV = {
  ...process.env,
  PYTHONDONTWRITEBYTECODE: process.env.PYTHONDONTWRITEBYTECODE || '1',
};

if (args.length === 0) {
  console.error('Usage: node tools/scripts/run-python.js <script.py> [args...]');
  process.exit(1);
}

function uniqueCandidates(candidates) {
  const seen = new Set();
  const unique = [];

  for (const candidate of candidates) {
    const key = candidate.join('\u0000');
    if (!seen.has(key)) {
      seen.add(key);
      unique.push(candidate);
    }
  }

  return unique;
}

function getPythonCandidates() {
  const configuredPython =
    process.env.ANTIGRAVITY_PYTHON || process.env.npm_config_python;
  
  const home = process.env.HOME || process.env.USERPROFILE || "";
  const localPythonPath = path.join(home, 'AppData', 'Local', 'Python', 'pythoncore-3.14-64', 'python.exe');

  const isWindows = process.platform === 'win32';
  const candidates = isWindows ? [
    [localPythonPath], // Pin the absolute AppData python path directly
    configuredPython ? [configuredPython] : null,
    ['python'],
    ['py', '-3'],
    ['python3'],
  ] : [
    configuredPython ? [configuredPython] : null,
    ['python3'],
    ['python'],
  ];

  return uniqueCandidates(candidates.filter(Boolean));
}

function canRun(candidate) {
  const [command, ...baseArgs] = candidate;
  
  // If absolute path, verify file existence first
  if (path.isAbsolute(command)) {
    if (!fs.existsSync(command)) {
      return false;
    }
  }

  try {
    const probe = spawnSync(
      command,
      [...baseArgs, '--version'],
      {
        env: PYTHON_ENV,
        stdio: 'ignore',
        shell: false, // Absolutely disable shell execution by default to avoid spaces parsing failures in USERPROFILE paths
      }
    );
    if (probe.error) {
      return false;
    }
    return probe.status === 0;
  } catch (err) {
    return false;
  }
}

const pythonCandidates = getPythonCandidates();
const selected = pythonCandidates.find(canRun);

if (!selected) {
  console.error(
    'Unable to find a valid Python 3 interpreter. Tried: python, python3, py -3',
  );
  process.exit(1);
}

const [command, ...baseArgs] = selected;
const child = spawn(command, [...baseArgs, ...args], {
  env: PYTHON_ENV,
  stdio: 'inherit',
  shell: false, // Avoid shell parsing of spaces in absolute paths on Windows!
});

child.on('error', (error) => {
  console.error(`Failed to start Python interpreter "${command}": ${error.message}`);
  process.exit(1);
});

child.on('exit', (code, signal) => {
  if (signal) {
    try {
      process.kill(process.pid, signal);
    } catch {
      process.exit(1);
    }
    return;
  }

  process.exit(code ?? 1);
});
