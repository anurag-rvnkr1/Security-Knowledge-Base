#!/usr/bin/env python3
"""Generate site/content.json from the repository's real Markdown tree.

Run from the repository root:
    python scripts/build-content-index.py

Standard library only. The generated JSON contains every Markdown path and is
safe to use with the static GitHub Pages portal.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'site'/'content.json'
SKIP={'.git','.github','node_modules','site','scripts'}
DESCRIPTIONS={
'API-Security':'API architecture, authentication, authorization, testing and monitoring.','Active-Directory':'Directory architecture, administration, security and blue-team practices.','CTF-Writeups':'Hands-on challenge writeups organized by security domain.','Cheatsheets':'Compact technical references for security workflows and tools.','Cloud-Security':'Cloud security concepts, controls, architecture and monitoring.','Containers':'Container architecture, security, hardening and runtime concepts.','Cryptography':'Cryptographic foundations, algorithms, protocols and applied security.','Detection-Engineering':'Telemetry, detection logic, validation, tuning and lifecycle practices.','DevSecOps':'Security integrated into development, CI/CD and software delivery.','Digital-Forensics':'Forensic evidence, artifacts, analysis and investigation workflows.','Email-Security':'Email threats, authentication, phishing analysis and defensive controls.','Endpoint-Security':'Endpoint visibility, hardening, monitoring and protection.','Identity-and-Access-Management':'Identity, authentication, authorization, access control and governance.','Incident-Response':'Incident preparation, triage, containment, recovery and investigation.','Kubernetes':'Kubernetes architecture, operations and cloud-native security.','Labs':'Controlled hands-on security exercises and practical worksheets.','Linux':'Linux administration, security, monitoring and defensive operations.','MITRE-ATTACK':'ATT&CK tactics, techniques, mapping and defensive context.','Malware-Analysis':'Malware analysis workflows, artifacts and defensive investigation.','Network-Security':'Network protection, monitoring, architecture and defensive controls.','Networking':'Networking fundamentals underpinning security operations.','OSINT':'Open-source intelligence collection, analysis and research workflows.','OWASP':'Application-security guidance, vulnerabilities and defensive practices.','Resources':'Courses, tools, standards, research and learning references.','Reverse-Engineering':'Reverse-engineering concepts and technical analysis.','SIEM':'Security monitoring, telemetry, analysis, detection and operations.','SOC':'Security operations, triage, alert handling and analyst workflows.','Security-Architecture':'Security architecture, design principles, controls and planning.','Security-Automation':'Automation patterns for repeatable security operations.','Threat-Hunting':'Hypothesis-driven hunting, telemetry, analysis and investigation.','Threat-Intelligence':'Threat intelligence collection, enrichment, analysis and use.','Vulnerability-Management':'Discovery, assessment, prioritization, remediation and lifecycle management.','Web-Security':'Web application security, vulnerabilities, testing and defensive practices.','Windows':'Windows administration, logging, security and hardening.'}
def human(s):
    s=re.sub(r'[-_]+',' ',s); s=re.sub(r'^\d+\s*','',s)
    return s.title().replace('Api','API').replace('Mitre','MITRE').replace('Owasp','OWASP').replace('Osint','OSINT').replace('Siem','SIEM').replace('Soc','SOC').replace('Iam','IAM')
def main():
    files=[]
    for p in ROOT.rglob('*.md'):
        rel=p.relative_to(ROOT)
        if any(part in SKIP for part in rel.parts): continue
        files.append(rel.as_posix())
    files.sort()
    roots=sorted({p.split('/')[0] for p in files})
    cats=[]
    for root in roots:
        docs=[]
        for path in files:
            if not path.startswith(root+'/'): continue
            stem=Path(path).stem
            docs.append({'title':human(stem),'path':path,'tags':[root],'kind':'template' if 'template' in stem.lower() else ('index' if stem.lower()=='readme' else 'document')})
        cats.append({'name':human(root),'path':root,'description':DESCRIPTIONS.get(root,f'Knowledge material covering {human(root)}.'),'icon':'book','documents':docs})
    roots_json={c['name'] for c in cats}
    payload={'version':1,'generatedFrom':'main','repository':'https://github.com/anurag-rvnkr1/Security-Knowledge-Base','pages':'https://anurag-rvnkr1.github.io/Security-Knowledge-Base/','stats':{'markdownDocuments':len(files)},'categories':cats}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f'Wrote {OUT}: {len(files)} Markdown documents across {len(cats)} collections.')
if __name__=='__main__': main()
