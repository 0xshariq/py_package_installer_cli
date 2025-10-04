#!/usr/bin/env python3
import subprocess
import sys
import os
import json
from pathlib import Path

def check_node_installed():
    """Check if Node.js is installed"""
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            return True
    except FileNotFoundError:
        pass
    return False

def check_npm_installed():
    """Check if npm is installed"""
    try:
        result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            return True
    except FileNotFoundError:
        pass
    return False

def install_dependencies():
    """Install Node.js dependencies if needed"""
    # Get the directory where this script is installed
    package_dir = Path(__file__).parent
    package_json_path = package_dir / "package.json"
    node_modules_path = package_dir / "node_modules"
    
    # Check if dependencies are already installed
    if node_modules_path.exists():
        return True
    
    if not package_json_path.exists():
        print("Warning: package.json not found. Some features may not work.")
        return False
    
    print("Installing Node.js dependencies for the first time...")
    print("This may take a few minutes...")
    
    try:
        # Change to package directory and install dependencies
        result = subprocess.run(
            ["npm", "install", "--production"],
            cwd=package_dir,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("Dependencies installed successfully!")
            return True
        else:
            print(f"Error installing dependencies: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        return False

def main():
    """Main entry point for the CLI"""
    # Check if Node.js is installed
    if not check_node_installed():
        print("Error: Node.js is not installed.")
        print("Please install Node.js from https://nodejs.org/")
        sys.exit(1)
    
    # Check if npm is installed
    if not check_npm_installed():
        print("Error: npm is not installed.")
        print("Please install npm (usually comes with Node.js)")
        sys.exit(1)
    
    # Install dependencies if needed
    if not install_dependencies():
        print("Warning: Could not install all dependencies. Some features may not work.")
    
    # Get the directory where this script is installed
    package_dir = Path(__file__).parent
    dist_path = package_dir / "dist" / "index.js"
    
    if not dist_path.exists():
        print(f"Error: Required file not found: {dist_path}")
        sys.exit(1)
    
    # Run the Node.js CLI
    try:
        subprocess.run(["node", str(dist_path)] + sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        print(f"Error running CLI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()