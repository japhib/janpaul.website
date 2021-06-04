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

# RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
# LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
disqus_code = """
<div id="disqus_thread"></div>
<script>
    var disqus_config = function () {
        this.page.url = location.href;
        this.page.identifier = '{{page_identifier}}';
    };
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://janpaulwebsite.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
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
            colon = line.index(': ')
            key = line[:colon]
            val = line[colon+2:]
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
    context["content"] = '<div class="content">' + file_contents + '</div>'

    # parse title from frontmatter
    if 'title' in frontmatter:
        # context["title"] = '<div class="page-title">' + frontmatter['title'] + '</div>'
        context["title"] = '<h1>' + frontmatter['title'] + '</h1>'
        context["head_title"] = ' - ' + frontmatter['title']
    else:
        context["title"] = ''
        context["head_title"] = ''

    # parse date from frontmatter
    if 'date' in frontmatter:
        context["date"] = '<p class="date">Published ' + frontmatter['date'] + '</p>'
    else:
        context["date"] = ''

    # parse description from frontmatter
    if 'description' in frontmatter:
        context["description"] = '<p class="subtitle">' + frontmatter['description'] + '</p>'
    else:
        context["description"] = ''
    
    # disqus
    if filename.startswith('src/blog/') and filename != 'src/blog/index.md':
        page_identifier = filename.replace('src/blog/', '')
        page_identifier = page_identifier.replace('.md', '')
        context['disqus'] = chevron.render(disqus_code, {'page_identifier': page_identifier})
    else:
        context['disqus'] = ''

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
    
    