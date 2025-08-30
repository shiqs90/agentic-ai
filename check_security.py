#!/usr/bin/env python3
"""
Security Verification Script for Live-Class Project

This script helps verify that the security setup is correct and no hardcoded API keys remain.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

# Patterns to search for potential API keys
SECURITY_PATTERNS = {
    'OpenAI API Key': r'sk-[a-zA-Z0-9]{20,}',
    'Pinecone API Key': r'pcsk_[a-zA-Z0-9_-]+',
    'Notion API Key': r'ntn_[a-zA-Z0-9]+',
    'Mem0 API Key': r'm0-[a-zA-Z0-9_-]+',
    'NGROK Token': r'["\'][0-9a-zA-Z]{48,}["\']',
    'Hardcoded Assignment': r'(api_key|apikey|secret|token)\s*=\s*["\'][^"\']{20,}["\']',
}

# Files to exclude from scanning
EXCLUDE_FILES = {
    'check_security.py',
    'SECURITY_SETUP.md',
    'env_template.txt',
    '.gitignore',
    'README.md'
}

# Directories to exclude
EXCLUDE_DIRS = {
    '.git',
    '__pycache__',
    '.venv',
    'venv',
    'env',
    'node_modules',
    '.ipynb_checkpoints'
}

def scan_file(file_path: Path) -> List[Tuple[str, int, str, str]]:
    """
    Scan a file for potential security issues.
    
    Returns:
        List of tuples: (pattern_name, line_number, line_content, match)
    """
    issues = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                for pattern_name, pattern in SECURITY_PATTERNS.items():
                    matches = re.findall(pattern, line, re.IGNORECASE)
                    for match in matches:
                        # Skip if it's a placeholder or environment variable reference
                        if any(placeholder in match.lower() for placeholder in [
                            'your_', 'placeholder', 'example', 'test', 'demo',
                            'os.getenv', 'getenv', 'environ'
                        ]):
                            continue
                        
                        issues.append((pattern_name, line_num, line.strip(), match))
    
    except Exception as e:
        print(f"Warning: Could not scan {file_path}: {e}")
    
    return issues

def scan_directory(directory: Path) -> List[Tuple[Path, str, int, str, str]]:
    """
    Recursively scan directory for security issues.
    
    Returns:
        List of tuples: (file_path, pattern_name, line_number, line_content, match)
    """
    all_issues = []
    
    for file_path in directory.rglob('*'):
        # Skip directories
        if file_path.is_dir():
            continue
            
        # Skip excluded directories
        if any(excluded in file_path.parts for excluded in EXCLUDE_DIRS):
            continue
            
        # Skip excluded files
        if file_path.name in EXCLUDE_FILES:
            continue
            
        # Only scan text files
        if file_path.suffix in {'.py', '.ipynb', '.json', '.txt', '.md', '.yml', '.yaml', '.env.example'}:
            issues = scan_file(file_path)
            for issue in issues:
                all_issues.append((file_path, *issue))
    
    return all_issues

def check_env_setup() -> bool:
    """Check if environment setup is correct."""
    print("🔍 Checking environment setup...")
    
    # Check if .env is in .gitignore
    gitignore_path = Path('.gitignore')
    if gitignore_path.exists():
        with open(gitignore_path, 'r') as f:
            gitignore_content = f.read()
            if '.env' in gitignore_content:
                print("✅ .env is properly listed in .gitignore")
            else:
                print("❌ .env is NOT in .gitignore - this is a security risk!")
                return False
    else:
        print("⚠️  .gitignore file not found")
    
    # Check if env_template.txt exists
    if Path('env_template.txt').exists():
        print("✅ env_template.txt found")
    else:
        print("⚠️  env_template.txt not found")
    
    # Check if .env exists (should exist but not be tracked)
    if Path('.env').exists():
        print("✅ .env file exists (good for local development)")
        print("⚠️  Make sure .env is never committed to git!")
    else:
        print("⚠️  .env file not found - you'll need to create it from the template")
    
    return True

def main():
    """Main security check function."""
    print("🔐 Live-Class Project Security Scanner")
    print("=" * 50)
    
    # Check environment setup
    env_ok = check_env_setup()
    print()
    
    # Scan for hardcoded secrets
    print("🔍 Scanning for hardcoded API keys and secrets...")
    current_dir = Path('.')
    issues = scan_directory(current_dir)
    
    if not issues:
        print("✅ No hardcoded API keys or secrets found!")
        print("✅ Security scan passed!")
        return 0
    else:
        print(f"❌ Found {len(issues)} potential security issues:")
        print()
        
        for file_path, pattern_name, line_num, line_content, match in issues:
            print(f"🚨 {file_path}:{line_num}")
            print(f"   Pattern: {pattern_name}")
            print(f"   Match: {match}")
            print(f"   Line: {line_content}")
            print()
        
        print("❌ Security scan failed!")
        print("Please review and fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 