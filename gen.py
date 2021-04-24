import glob
import chevron
import markdown2
import re

def readfile(filename):
    with open(filename, 'r') as file:
        return file.read()

template = readfile("layout/template.html")
head = readfile("layout/head.html")
header = readfile("layout/header.html")

context = {
    'head': head,
    'header': header
}

allfiles = glob.glob("src/**", recursive=True)
for filename in allfiles:
    if not filename.endswith('.md'):
        continue

    file_lines = readfile(filename).split('\n')

    # convert markdown to html
    # ... or, lines starting with // are kept as-is
    converted_lines = []
    for line in file_lines:
        if line.startswith("//"):
            converted_lines.append(line[2:])
        else:
            converted_lines.append(markdown2.markdown(line))
    file_contents = "\n".join(converted_lines)

    # render it as "content" in the template
    context["content"] = file_contents
    rendered = chevron.render(template, context)

    # remove "src/" from beginning of filename
    trimmed_filename = filename[4:]
    # change extension ".md" to ".html"
    trimmed_filename = re.sub(r'\.md$', '.html', trimmed_filename)

    # now write it out
    with open("public/" + trimmed_filename, 'w') as file:
        file.write(rendered)
    
    