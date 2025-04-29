from diagrams import Diagram, Cluster
from diagrams.generic.blank import Blank


def context_diagram():
    with Diagram("C4 Context", filename="c4_context", outformat="png", show=False):
        developer = Blank("Engineer / Contributor")
        repo = Blank("AI Delivery Framework Repo")
        developer >> repo


def container_diagram():
    with Diagram("C4 Container", filename="c4_container", outformat="png", show=False):
        repo = Blank("AI Delivery Framework Repo")
        with Cluster("Top-level Directories"):
            core = Blank("core/")
            prompts = Blank("prompts/")
            docs = Blank("docs/")
            scripts = Blank("scripts/")
            github = Blank(".github/")
        repo >> [core, prompts, docs, scripts, github]


def component_diagram():
    with Diagram("C4 Component", filename="c4_component", outformat="png", show=False):
        with Cluster("Governance Core"):
            codebase_guide = Blank("core/codebase_guide.md")
            scope_template = Blank("core/scope_doc_template.md")
            
            with Cluster("Context Wrappers"):
                tier0 = Blank("tier0_exploration")
                tier1 = Blank("tier1_hobby")
                tier2 = Blank("tier2_mvp")
                tier3 = Blank("tier3_beta")
                tier4 = Blank("tier4_production")
                tier5 = Blank("tier5_enterprise")
            
            with Cluster("Engine"):
                governance = Blank("governance_core.md")
                assurance = Blank("assurance_core.md")
        
        with Cluster("Documentation"):
            intro = Blank("introduction.md")
            tiers = Blank("delivery_tiers.md")
            arch = Blank("architecture/")
        
        with Cluster("Tools"):
            scripts_dir = Blank("scripts/")
        
        with Cluster("Prompts"):
            codebase_update = Blank("codebase_guide_update_template.md")
        
        codebase_guide >> [intro, tiers]
        codebase_guide >> [governance, assurance]
        scope_template >> [tier0, tier1, tier2, tier3, tier4, tier5]
        codebase_update >> codebase_guide
        scripts_dir >> codebase_guide


def main():
    context_diagram()
    container_diagram()
    component_diagram()


if __name__ == "__main__":
    main() 