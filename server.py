import mcp
from mcp.server.fastmcp import FastMCP
import httpx
import requests
import os
import base64

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = "chdaouihamza"
REPO = "projet-mcp"
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

mcp = FastMCP("Elyora MCP")
RESOURCE_CACHE: dict[str, str] = {}

def fetch_github_doc(filepath: str) -> str:
    """Télécharge le contenu brut d'un fichier Markdown depuis le dépôt GitHub."""
    if filepath in RESOURCE_CACHE:
        return RESOURCE_CACHE[filepath]

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{filepath}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return f"# Erreur\nImpossible de récupérer `{filepath}` : {response.json().get('message', 'erreur inconnue')}"

    data = response.json()
    content = base64.b64decode(data["content"]).decode("utf-8")

    RESOURCE_CACHE[filepath] = content
    return content


@mcp.resource("elyora://docs/manifest", mime_type="text/markdown")
def lire_manifeste() -> str:
    """Ressource : Fournit le contexte global, l'architecture générale et le but du projet Elyora."""
    return fetch_github_doc("ressources/manifest.md")


@mcp.resource("elyora://docs/architecture", mime_type="text/markdown")
def lire_architecture() -> str:
    """Ressource : Fournit les règles strictes de codage (PHP, Java, C++) et de sécurité (PDO, Hash)."""
    return fetch_github_doc("ressources/architecture.md")


@mcp.resource("elyora://docs/database", mime_type="text/markdown")
def lire_database() -> str:
    """Ressource : Fournit le dictionnaire de données SQL complet et les contraintes (ON DELETE CASCADE)."""
    return fetch_github_doc("ressources/database.md")


@mcp.resource("elyora://docs/business-logic", mime_type="text/markdown")
def lire_business_logic() -> str:
    """Ressource : Fournit les algorithmes métier (calcul des prix, taxes, règles de transport et budget)."""
    return fetch_github_doc("ressources/business_logic.md")


@mcp.resource("elyora://docs/ui-guidelines", mime_type="text/markdown")
def lire_ui_guidelines() -> str:
    """Ressource : Fournit la charte graphique (CSS, couleurs primaires, bordures) et les règles JS."""
    return fetch_github_doc("ressources/ui_guidelines.md")


@mcp.tool()
def get_pr_metadata(pr_number: int):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return {"error": response.json()}

    pr = response.json()

    return {
        "number": pr["number"],
        "title": pr["title"],
        "author": pr["user"]["login"],
        "target_branch": pr["base"]["ref"],
        "source_branch": pr["head"]["ref"],
        "labels": [label["name"] for label in pr["labels"]],
        "state": pr["state"],
    }


@mcp.tool()
def list_pr_comments(pr_number: int):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}/comments"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return {"error": response.json()}
    return response.json()


@mcp.tool()
def list_pr_reviews(pr_number: int):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}/reviews"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return {"error": response.json()}
    return response.json()


@mcp.tool()
def get_file_changes(pr_number: int, filepath: str):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}/files"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return {"error": response.json()}

    files = response.json()
    for file in files:
        if file["filename"] == filepath:
            return file

    return {"error": "File not found"}


@mcp.tool()
def check_merge_conflicts(pr_number: int):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return {"error": response.json()}

    pr = response.json()
    return {
        "mergeable": pr["mergeable"],
        "mergeable_state": pr["mergeable_state"],
    }


@mcp.tool()
def get_ci_status(pr_number: int):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    commits = httpx.get(url, headers=HEADERS).json()
    sha = commits[0]["sha"]

    checks_url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits/{sha}/check-runs"
    response = httpx.get(checks_url, headers=HEADERS)
    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()


@mcp.tool()
def post_pr_comment(pr_number: int, message: str):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{pr_number}/comments"
    body = {"body": message}
    response = requests.post(url, headers=HEADERS, json=body)
    return response.json()


@mcp.tool()
def get_contributing_guidelines():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/CONTRIBUTING.md"
    response = requests.get(url, headers=HEADERS)
    return response.json()


with open("prompts/check_pr_health.md") as f:
    PR_HEALTH_TEMPLATE = f.read()

@mcp.prompt(
    name="check-pr-health",
    description="Analyse la santé d'une PR du repo Elyora avant merge"
)
def check_pr_health(pr_number: str, strictness_level: str = "standard", additional_instructions: str = "") -> str:
    return PR_HEALTH_TEMPLATE.format(
        pr_number=pr_number,
        strictness_level=strictness_level,
        additional_instructions=additional_instructions
    )


if __name__ == "__main__":
    mcp.run()
