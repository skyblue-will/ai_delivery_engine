from diagrams import Diagram, Cluster
from diagrams.generic.blank import Blank


def context_diagram():
    with Diagram("C4 Context", filename="docs/architecture/c4_context", outformat="png", show=False):
        developer = Blank("Engineer / Contributor")
        repo = Blank("AI Delivery Framework Repo")
        developer >> repo


def container_diagram():
    with Diagram("C4 Container", filename="docs/architecture/c4_container", outformat="png", show=False):
        repo = Blank("AI Delivery Framework Repo")
        with Cluster("Top-level Directories"):
            meta = Blank("meta/")
            docs = Blank("docs/")
            tools = Blank("tools/")
            examples = Blank("examples/")
            branding = Blank("branding/")
        repo >> [meta, docs, tools, examples, branding]


def component_diagram():
    with Diagram("C4 Component", filename="docs/architecture/c4_component", outformat="png", show=False):
        with Cluster("meta/"):
            codebase = Blank("codebase_guide_template.md")
            scope = Blank("scope_doc_template.md")
            wrappers = Blank("context_wrappers/")
        docs_dir = Blank("docs/")
        tools_dir = Blank("tools/")
        examples_dir = Blank("examples/")
        codebase >> docs_dir
        scope >> tools_dir
        wrappers >> examples_dir


def main():
    context_diagram()
    container_diagram()
    component_diagram()


if __name__ == "__main__":
    main() 