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
    'header': header
}

allfiles = glob.glob("src/**", recursive=True)
for filename in allfiles:
    if not filename.endswith('.md'):
        continue

    file_lines = readfile(filename).split('\n')


    # convert markdown to html
    converted_lines = []
    in_frontmatter = False
    frontmatter = {}
    for line in file_lines:
        # -- signals start or end of frontmatter section
        if line.startswith("--"):
            in_frontmatter = not in_frontmatter

        # parse frontmatter keys like title, date, draft status
        elif in_frontmatter:
            items = line.split(': ')
            key = items[0]
            val = items[1]
            frontmatter[key] = val

        # lines starting with // are kept as-is
        elif line.startswith("//"):
            converted_lines.append(line[2:])

        # special code {rungame} turns into "Run Game" button
        elif "{rungame}" in line:
            converted_lines.append(re.sub(r'\{rungame\}', rungamebutton, line))

        # everything else is markdown translated to html
        else:
            converted_lines.append(markdown2.markdown(line))

    file_contents = "\n".join(converted_lines)
    context["content"] = file_contents

    # parse title from frontmatter
    if 'title' in frontmatter:
        context["title"] = '<div class="page-title">' + frontmatter['title'] + '</div>'
        context["head_title"] = ' - ' + frontmatter['title']
    else:
        context["title"] = ''
        context["head_title"] = ''

    # parse date from frontmatter
    if 'date' in frontmatter:
        context["date"] = 'Published on: ' + frontmatter['date']
    else:
        context["date"] = ''

    # parse description from frontmatter
    if 'description' in frontmatter:
        context["description"] = '<div class="centered">' + frontmatter['description'] + '</div>'
    else:
        context["description"] = ''

    # render context into the head of the template (template within a template)
    context['head'] = chevron.render(head, context)
    
    # now actually render
    rendered = chevron.render(template, context)

    # remove "src/" from beginning of filename
    trimmed_filename = filename[4:]
    # change extension ".md" to ".html"
    trimmed_filename = re.sub(r'\.md$', '.html', trimmed_filename)

    # now write it out
    with open("public/" + trimmed_filename, 'w') as file:
        file.write(rendered)
    
    