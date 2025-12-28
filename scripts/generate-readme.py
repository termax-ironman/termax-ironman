import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILE_FILE = ROOT / "profile.yaml"
README_FILE = ROOT / "README.md"

START = "<!-- AUTO-GENERATED-START -->"
END = "<!-- AUTO-GENERATED-END -->"


def load_yaml():
    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def generate_section(data):
    profile = data.get("profile", {})
    links = data.get("links", {})
    tech = data.get("tech_stack", {})
    projects = data.get("projects", [])
    problem = data.get("problem_solving", {})
    learning = data.get("learning", {})
    goals = data.get("goals", {})
    contact = data.get("contact", {})

    out = []

    out.append(f"# 👋 {profile.get('name','')}\n")
    out.append(f"**{profile.get('tagline','')}**\n")

    if profile.get("summary"):
        out.append(profile["summary"] + "\n")

    if links.get("leetcode"):
        out.append("## 🔗 Profiles\n")
        out.append(f"- 🧠 LeetCode: {links['leetcode']}\n")

    out.append("## 🛠 Tech Stack\n")

    for title, key in [
        ("Languages", "languages"),
        ("Frameworks", "frameworks"),
        ("Microservices & APIs", "microservices"),
        ("AI & Agent Systems", "ai_and_agents"),
        ("Databases", "databases"),
        ("Tools", "tools"),
        ("Cloud & DevOps", "cloud_devops"),
    ]:
        if key in tech:
            out.append(f"### {title}\n")
            out.append(bullets(tech[key]) + "\n")

    if projects:
        out.append("## 📂 Projects\n")
        for p in projects:
            out.append(f"### {p.get('category','')}\n")
            out.append(bullets(p.get("details", [])) + "\n")

    if problem:
        out.append("## 🧠 DSA & Problem Solving\n")
        if problem.get("platform"):
            out.append(f"- Platform: {problem['platform']}\n")
        if problem.get("profile_url"):
            out.append(f"- Profile: {problem['profile_url']}\n")
        if problem.get("focus"):
            out.append("\n### Focus Areas\n")
            out.append(bullets(problem["focus"]) + "\n")

    if learning.get("current"):
        out.append("## 📚 Currently Learning\n")
        out.append(bullets(learning["current"]) + "\n")

    if goals:
        out.append("## 🎯 Goals\n")
        if goals.get("short_term"):
            out.append("### Short Term\n")
            out.append(bullets(goals["short_term"]) + "\n")
        if goals.get("long_term"):
            out.append("### Long Term\n")
            out.append(bullets(goals["long_term"]) + "\n")

    if contact:
        out.append("## 🤝 Collaboration\n")
        out.append(bullets(contact.get("collaboration", [])) + "\n")
        if contact.get("note"):
            out.append(contact["note"] + "\n")

    out.append(
        "\n---\n"
        "⭐ This section is **auto-generated** from `profile.yaml`.\n"
    )

    return "\n".join(out)


def update_readme(auto_content):
    readme = README_FILE.read_text(encoding="utf-8")

    if START not in readme or END not in readme:
        raise RuntimeError("AUTO-GENERATED markers not found in README.md")

    before = readme.split(START)[0]
    after = readme.split(END)[1]

    new_readme = (
        before
        + START
        + "\n"
        + auto_content
        + "\n"
        + END
        + after
    )

    README_FILE.write_text(new_readme, encoding="utf-8")


if __name__ == "__main__":
    data = load_yaml()
    section = generate_section(data)
    update_readme(section)
    print("✅ README updated (header preserved)")
