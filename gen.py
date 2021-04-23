import glob
import chevron

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
    if not filename.endswith('.html'):
        continue

    file_contents = readfile(filename)

    # append <br /> to each line
    file_contents = "<br />\n".join(file_contents.split('\n'))

    # render it as "content" in the template
    context["content"] = file_contents
    rendered = chevron.render(template, context)

    # remove "src/" from beginning of filename
    trimmed_filename = filename[4:]

    # now write it out
    with open("public/" + trimmed_filename, 'w') as file:
        file.write(rendered)
    
    