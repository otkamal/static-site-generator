import os
import mdprocessing

def extract_title(markdown: str) -> str:
    first_header = markdown.split("\n")[0]
    first_h1 = first_header.split("#")
    if len(first_h1) != 2:
        raise TypeError("could not find h1")
    h1_text = first_h1[1].strip()
    return h1_text

def generate_page(from_path: str, to_path: str, template_path: str) -> None:
    print(f"Generating page from {from_path} to {to_path} using {template_path}.")
    with open(from_path) as f:
        with open(template_path) as t:
            markdown = f.read()
            template = t.read()
            markdown_as_nodes = mdprocessing.markdown_to_HTMLNode(markdown)
            markdown_as_html = markdown_as_nodes.to_html()
            template = template.replace("{{ Content }}", markdown_as_html)
            template = template.replace("{{ Title }}", extract_title(markdown))
            with open(to_path, "w") as copy:
                 copy.write(template)

def generate_page_recursive(src: str, dest: str, template_path: str) -> None:
    for path in os.listdir(src):
        old_path = os.path.join(src, path)
        new_path = os.path.join(dest, path.replace(".md", ".html"))
        if os.path.isfile(old_path):
            generate_page(old_path, new_path, template_path)
        else:
            os.mkdir(new_path)
            generate_page_recursive(old_path, new_path, template_path)