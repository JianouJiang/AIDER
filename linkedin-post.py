#!/usr/bin/env python3
"""
LinkedIn Post for AIDER — AI-Driven Energy Research Journal

Posts to LinkedIn using the UGC Posts API v2.
Credentials loaded from proxima-auto-company/.env (shared LinkedIn account).

Usage:
    python3 linkedin-post.py
"""

import os
import requests
from pathlib import Path

# Load .env from proxima-auto-company (where LinkedIn credentials live)
env_path = Path(__file__).parent.parent / "proxima-auto-company" / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")
PERSON_URN = os.environ.get("LINKEDIN_PERSON_URN")

if not ACCESS_TOKEN or not PERSON_URN:
    print("ERROR: Missing LINKEDIN_ACCESS_TOKEN or LINKEDIN_PERSON_URN in .env")
    exit(1)

# ─── Post Content ───────────────────────────────────────────────

POST_TEXT = """Launching AIDER — AI-Driven Energy Research, a new diamond open-access journal. https://ai-driven-energy-research.github.io/

I'm a DPhil candidate at Oxford and I kept seeing the same problem in energy research: papers locked behind paywalls, code never shared, results impossible to reproduce, and AI assistance treated like a dirty secret.

So I started a journal that fixes all of that:

What makes AIDER different:
- Every paper must include code, data, and full methodology — no exceptions
- AI-assisted research is embraced and must be disclosed, not hidden
- Papers live as GitHub repositories — fork them, run them, extend them
- Automated reproducibility checks run on every submission
- Free to read, free to publish — no paywalls, no author fees, ever

Scope: AI applications in energy systems — ML for CFD, AI-driven grid optimisation, reinforcement learning for control, foundation models for energy, generative models for materials discovery, and more.

We're building the editorial board now and preparing our founding papers. ISSN application is filed with the British Library.

If you work at the intersection of AI and energy, I'd love for you to get involved — as an author, reviewer, or editorial board member.

Website: https://ai-driven-energy-research.github.io/
Submit: https://github.com/ai-driven-energy-research/submissions

#OpenAccess #AcademicPublishing #EnergyResearch #ArtificialIntelligence #OpenScience #Reproducibility #MachineLearning #CFD #CleanEnergy"""

# ─── Post to LinkedIn ───────────────────────────────────────────

url = "https://api.linkedin.com/v2/ugcPosts"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0",
}

payload = {
    "author": f"urn:li:person:{PERSON_URN.split(':')[-1]}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": POST_TEXT
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

print("Posting to LinkedIn...")
print(f"Author URN: {PERSON_URN}")
print(f"Post length: {len(POST_TEXT)} characters")
print("-" * 60)

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 201:
    result = response.json()
    print(f"SUCCESS: LinkedIn post published!")
    print(f"Response: {result}")
    post_id = result.get("id", "")
    if post_id:
        share_id = post_id.split(":")[-1]
        print(f"\nView post: https://www.linkedin.com/feed/update/{post_id}")
else:
    print(f"FAILED: HTTP {response.status_code}")
    print(f"Response: {response.text}")
