# 📦 Package Installer CLI

[![PyPI version](https://img.shields.io/pypi/v/package-installer-cli.svg)](https://pypi.org/project/package-installer-cli/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-%3E%3D3.8-brightgreen.svg)](https://python.org/)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18.0.0-brightgreen.svg)](https://nodejs.org/)

A **cross-platform, interactive CLI** to scaffold modern web application templates with support for multiple frameworks, languages, and development tools. Create production-ready projects in seconds!

## 🚀 Quick Features

- **🎨 Multiple Frameworks**: React, Next.js, Express, Angular, Vue, Rust
- **🔤 Language Support**: TypeScript & JavaScript variants
- **🎭 UI Libraries**: Tailwind CSS, Material-UI, shadcn/ui
- **📦 Smart Package Management**: Auto-detects npm, yarn, pnpm
- **⚡ Lightning Fast**: Optimized template generation with intelligent caching
- **🌈 Beautiful CLI**: Gorgeous terminal interface with real-time analytics
- **🔍 Project Analysis**: Advanced dependency analysis and project insights

## ✨ New Features

- **📊 Enhanced Analytics Dashboard**: Real-time usage analytics with detailed insights
- **🎯 Smart Dependency Updates**: Project-specific dependency management for JS, Python, Rust, Go, Ruby, PHP
- **🚀 Intelligent CLI Upgrades**: Separate upgrade system with breaking change detection
- **💾 .package-installer-cli Folder**: All cache and history stored in dedicated folder
- **📈 Usage Tracking**: Comprehensive command and feature usage tracking
- **⚡ Performance Insights**: Productivity scoring and usage patterns

## 📥 Installation

### Global Installation (Recommended)
```bash
# Using pip (system-wide)
pip install package-installer-cli

# Using pip3 (system-wide)
pip3 install package-installer-cli
```

### Local/User Installation
```bash
# Install for current user only
pip install --user package-installer-cli

# Using pip3 for current user only
pip3 install --user package-installer-cli
```

**Note**: If you use `--user`, make sure `~/.local/bin` (Linux/Mac) or `%APPDATA%\Python\Scripts` (Windows) is in your PATH.

## 🎯 Quick Start

```bash
# Create new project interactively
pi create

# Analyze project with enhanced dashboard
pi analyze

# Update project dependencies only
pi update

# Upgrade CLI to latest version
pi upgrade-cli
```

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [📋 Commands](https://github.com/0xshariq/package-installer-cli/tree/main/docs/commands.md) | Complete command reference with examples |
| [⚡ Features](https://github.com/0xshariq/package-installer-cli/tree/main/docs/features.md) | Detailed feature documentation and usage |
| [🎨 Templates](https://github.com/0xshariq/package-installer-cli/tree/main/docs/templates.md) | Available templates and customization options |
| [🚀 Deployment](https://github.com/0xshariq/package-installer-cli/tree/main/docs/deploy.md) | Deployment options and platform integration |

## 🛠️ Command Overview

| Command | Description | Usage |
|---------|-------------|-------|
| `pi create` | Create new project from templates | `pi create [name]` |
| `pi analyze` | Enhanced project analytics dashboard | `pi analyze [--detailed]` |
| `pi update` | Update project dependencies | `pi update [--latest]` |
| `pi upgrade-cli` | Upgrade CLI to latest version | `pi upgrade-cli` |
| `pi add` | Add features to existing projects | `pi add [feature]` |
| `pi doctor` | Diagnose and fix project issues | `pi doctor` |
| `pi clean` | Clean development artifacts | `pi clean [--all]` |

*For complete command documentation, see [commands](https://github.com/0xshariq/package-installer-cli/tree/main/docs/commands.md)*

## 🏗️ Supported Project Types

| Language/Framework | Templates | Package Managers |
|-------------------|-----------|------------------|
| **JavaScript/TypeScript** | React, Next.js, Express, Angular, Vue | npm, yarn, pnpm |
| **Python** | Django, Flask, FastAPI | pip, poetry |
| **Rust** | Basic, Advanced, Web | cargo |
| **Go** | CLI, Web, API | go mod |
| **Ruby** | Rails, Sinatra | bundler |
| **PHP** | Laravel, Symfony | composer |

*For detailed template information, see [templates](https://github.com/0xshariq/package-installer-cli/tree/main/docs/templates.md)*

## 🎯 System Requirements

- **Python**: 3.8 or higher
- **Node.js**: 18.0.0 or higher (required for the underlying CLI)
- **Operating Systems**: Windows, macOS, Linux
- **Package Managers**: npm, yarn, or pnpm
- **Git**: Required for project initialization

## ⚡ Node.js Dependency Management

### 🔄 Automatic Installation (Default)
When you first run any CLI command, Node.js dependencies are **automatically installed**:

```bash
# First time usage - auto-installs dependencies
package-installer create nextjs my-app
```

The CLI will automatically run `npm install --production` in the package directory.

### 🛠️ Manual Installation (If Auto-Install Fails)

If you see this message:
```
[!] Automatic installation of Node.js dependencies failed.
============================================================
To use all features of this CLI, please manually install dependencies:

1. Navigate to the package directory:
   cd /path/to/package/directory

2. Install dependencies:
   npm install --production

3. Re-run your CLI command
============================================================
```

#### For Global Installation:
```bash
# Find package location
pip show package-installer-cli | grep Location

# Navigate to package directory
cd /usr/local/lib/python3.x/site-packages/package_installer_cli
# OR (depending on your system)
cd /home/username/.local/lib/python3.x/site-packages/package_installer_cli

# Install dependencies
npm install --production
```

#### For Local/User Installation:
```bash
# Navigate to user package directory
cd ~/.local/lib/python3.x/site-packages/package_installer_cli

# Install dependencies
npm install --production
```

#### Common Package Locations:
- **Linux Global**: `/usr/local/lib/python3.x/site-packages/`
- **Linux User**: `~/.local/lib/python3.x/site-packages/`
- **macOS Global**: `/usr/local/lib/python3.x/site-packages/`
- **macOS User**: `~/Library/Python/3.x/lib/python/site-packages/`
- **Windows Global**: `C:\Python3x\Lib\site-packages\`
- **Windows User**: `%APPDATA%\Python\Python3x\site-packages\`

### 🚨 Prerequisites
Make sure you have Node.js and npm installed:
```bash
# Check versions
node --version    # Should be >= 18.0.0
npm --version     # Should be >= 8.0.0

# Install Node.js if missing
# Visit: https://nodejs.org/
```

## 🐛 Troubleshooting

### Quick Fixes

#### Python Package Issues
```bash
# Clear cache and reinstall (global)
pip uninstall package-installer-cli
pip install package-installer-cli

# Clear cache and reinstall (user)
pip uninstall package-installer-cli
pip install --user package-installer-cli
```

#### Node.js Dependency Issues
```bash
# Find your package installation directory
pip show package-installer-cli | grep Location

# Navigate to that directory + package_installer_cli folder
cd <Location>/package_installer_cli

# Clean install dependencies
rm -rf node_modules package-lock.json
npm install --production

# Verify installation
ls node_modules  # Should show installed packages
```

#### PATH Issues (User Installation)
If `package-installer` command is not found after `--user` installation:

**Linux/macOS:**
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Windows:**
Add `%APPDATA%\Python\Scripts` to your PATH environment variable.

#### Permission Issues (Global Installation)
```bash
# Try user installation instead
pip install --user package-installer-cli

# Or use sudo (Linux/macOS)
sudo pip install package-installer-cli
```

#### Complete Reset
```bash
# Remove everything and start fresh
pip uninstall package-installer-cli
pip cache purge
pip install package-installer-cli
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/0xshariq/package-installer-cli/tree/main/CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **PyPI Package**: [package-installer-cli](https://pypi.org/project/package-installer-cli/)
- **GitHub Repository**: [py_package_installer_cli](https://github.com/0xshariq/py_package_installer_cli)
- **Issues & Feedback**: [GitHub Issues](https://github.com/0xshariq/py_package_installer_cli/issues)

---

**Happy coding! 🚀** Create something amazing with Package Installer CLI.
