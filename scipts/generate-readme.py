import yaml

with open("profile.yaml") as f:
    data = yaml.safe_load(f)

def list_section(items):
    return "\n".join(f"- {item}" for item in items)

readme = f"""
# 👋 {data['profile']['name']}

**{data['profile']['tagline']}**

---

## 🔗 Profiles
- 🧠 LeetCode: {data['links']['leetcode']}

---

## 🛠 Tech Stack

### Languages
{list_section(data['tech']['languages'])}

### Frameworks
{list_section(data['tech']['frameworks'])}

### APIs & Communication
{list_section(data['tech']['apis'])}

### AI & Agent Systems
{list_section(data['tech']['ai'])}

---

⭐ This README is automatically generated from `profile.yaml`
"""

with open("README.md", "w") as f:
    f.write(readme.strip())

print("README.md generated successfully")
