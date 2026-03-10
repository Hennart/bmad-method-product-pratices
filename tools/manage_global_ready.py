#!/usr/bin/env python3
"""
ADEO Global Ready Requirements Manager
Helper script to manage the Global Ready requirements CSV file
"""

import csv
import sys
from pathlib import Path
from collections import defaultdict

CSV_FILE = Path(__file__).parent.parent / "data" / "2026-Global-Ready-Requirements.csv"

def load_requirements():
    """Load requirements from CSV"""
    requirements = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            requirements.append(row)
    return requirements

def save_requirements(requirements):
    """Save requirements to CSV"""
    if not requirements:
        print("❌ No requirements to save")
        return
    
    fieldnames = requirements[0].keys()
    with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(requirements)
    print(f"✅ Saved {len(requirements)} requirements to {CSV_FILE}")

def list_domains():
    """List all domains"""
    requirements = load_requirements()
    domains = defaultdict(int)
    for req in requirements:
        domains[req['Domain']] += 1
    
    print("\n📊 Domains:")
    for domain, count in sorted(domains.items()):
        print(f"  - {domain}: {count} requirements")

def list_by_domain(domain):
    """List requirements for a specific domain"""
    requirements = load_requirements()
    filtered = [r for r in requirements if r['Domain'] == domain]
    
    if not filtered:
        print(f"❌ No requirements found for domain: {domain}")
        return
    
    print(f"\n📋 Requirements for {domain}:")
    for req in filtered:
        status = req.get('Assessment', '').strip() or '⚪'
        if status == 'YES':
            status = '✅'
        elif status == 'NO':
            status = '❌'
        elif status == 'NOT APPLICABLE':
            status = '⊘'
        
        print(f"  {status} [{req['#']}] {req['Requirement']} (Level {req['Level']})")

def search_requirements(query):
    """Search requirements by keyword"""
    requirements = load_requirements()
    query_lower = query.lower()
    
    results = [
        r for r in requirements 
        if query_lower in r['#'].lower() 
        or query_lower in r['Requirement'].lower()
        or query_lower in r['Description'].lower()
    ]
    
    if not results:
        print(f"❌ No requirements found matching: {query}")
        return
    
    print(f"\n🔍 Found {len(results)} requirement(s):")
    for req in results:
        print(f"\n  ID: {req['#']}")
        print(f"  Name: {req['Requirement']}")
        print(f"  Domain: {req['Domain']} > {req['Topic']}")
        print(f"  Level: {req['Level']}")
        print(f"  Description: {req['Description'][:100]}...")
        if req.get('Assessment'):
            print(f"  Status: {req['Assessment']}")

def update_assessment(req_id, status, comment="", issue_keys=""):
    """Update assessment status for a requirement"""
    if status not in ['YES', 'NO', 'NOT APPLICABLE', '']:
        print(f"❌ Invalid status: {status}")
        print("Valid statuses: YES, NO, NOT APPLICABLE, or empty")
        return
    
    requirements = load_requirements()
    found = False
    
    for req in requirements:
        if req['#'] == req_id:
            req['Assessment'] = status
            if comment:
                req['Comment / Precision'] = comment
            if issue_keys:
                req['Issue Keys'] = issue_keys
            found = True
            break
    
    if not found:
        print(f"❌ Requirement not found: {req_id}")
        return
    
    save_requirements(requirements)
    print(f"✅ Updated {req_id} → {status}")
    if comment:
        print(f"   Comment: {comment}")
    if issue_keys:
        print(f"   Issues: {issue_keys}")

def stats():
    """Show statistics"""
    requirements = load_requirements()
    
    total = len(requirements)
    by_domain = defaultdict(int)
    by_level = defaultdict(int)
    by_status = defaultdict(int)
    
    for req in requirements:
        by_domain[req['Domain']] += 1
        by_level[req['Level']] += 1
        status = req.get('Assessment', '').strip()
        if status:
            by_status[status] += 1
        else:
            by_status['Not Assessed'] += 1
    
    print(f"\n📊 Global Ready Requirements Statistics")
    print(f"=" * 50)
    print(f"\nTotal Requirements: {total}")
    
    print(f"\n📁 By Domain:")
    for domain, count in sorted(by_domain.items()):
        pct = (count / total) * 100
        print(f"  {domain:.<30} {count:>3} ({pct:>5.1f}%)")
    
    print(f"\n📊 By Maturity Level:")
    for level, count in sorted(by_level.items()):
        pct = (count / total) * 100
        print(f"  Level {level} {count:>3} ({pct:>5.1f}%)")
    
    print(f"\n✅ Assessment Status:")
    for status, count in sorted(by_status.items()):
        pct = (count / total) * 100
        print(f"  {status:.<30} {count:>3} ({pct:>5.1f}%)")

def main():
    """Main CLI"""
    if len(sys.argv) < 2:
        print("""
🔧 ADEO Global Ready Requirements Manager

Usage:
  python manage_global_ready.py <command> [arguments]

Commands:
  domains                    List all domains
  list <domain>              List requirements for a domain
  search <query>             Search requirements by keyword
  update <id> <status>       Update requirement assessment
         [comment] [issues]  Optional: add comment and issue keys
  stats                      Show statistics

Examples:
  python manage_global_ready.py domains
  python manage_global_ready.py list Security
  python manage_global_ready.py search "IAM"
  python manage_global_ready.py update SEC-IAM-#10 YES "Implemented" "GOT-1234"
  python manage_global_ready.py stats
        """)
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'domains':
        list_domains()
    elif command == 'list' and len(sys.argv) >= 3:
        list_by_domain(sys.argv[2])
    elif command == 'search' and len(sys.argv) >= 3:
        search_requirements(sys.argv[2])
    elif command == 'update' and len(sys.argv) >= 4:
        req_id = sys.argv[2]
        status = sys.argv[3]
        comment = sys.argv[4] if len(sys.argv) > 4 else ""
        issues = sys.argv[5] if len(sys.argv) > 5 else ""
        update_assessment(req_id, status, comment, issues)
    elif command == 'stats':
        stats()
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
