import glob
import chevron
import markdown2
import re

rungamebutton = """
<button class="button run_game_btn">
    <svg stroke-linecap="round" stroke="currentColor" class="svgicon icon_play" role="img" version="1.1"
        viewBox="0 0 24 24" stroke-width="2" height="24" stroke-linejoin="round" aria-hidden="" fill="none" width="24">
        <circle cx="12" cy="12" r="10"></circle>
        <polygon points="10 8 16 12 10 16 10 8"></polygon>
    </svg>
    Run game
</button>
"""

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
        elif "{rungame}" in line:
            # special code {rungame} turns into "Run Game" button
            converted_lines.append(re.sub(r'\{rungame\}', rungamebutton, line))
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
    
    