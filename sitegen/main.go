package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"

	"github.com/cbroglie/mustache"
	"github.com/gomarkdown/markdown"
)

const rungamebtnHtml = `
<button class="button run_game_btn">
    <svg stroke-linecap="round" stroke="currentColor" class="svgicon icon_play" role="img" version="1.1"
        viewBox="0 0 24 24" stroke-width="2" height="24" stroke-linejoin="round" aria-hidden="" fill="none" width="24">
        <circle cx="12" cy="12" r="10"></circle>
        <polygon points="10 8 16 12 10 16 10 8"></polygon>
    </svg>
    Run game
</button>
`

var template, head, header string

func main() {
	template, head, header = readTemplateFiles()

	allfiles, err := getFilenamesRecursive("../src")
	if err != nil {
		panic(err)
	}

	for _, filename := range allfiles {
		if !strings.HasSuffix(filename, ".md") {
			continue
		}

		// remove "../src/" from beginning of filename
		// and change extension from ".md" to ".html"
		outputFilename := filename[7:len(filename)-3] + ".html"

		fileContents, _, frontmatter := parseFile(filename)

		context := make(map[string]string)

		// parse various fields from frontmatter
		if title, ok := frontmatter["title"]; ok {
			context["title"] = "<h1>" + title + "</h1>"
			context["head_title"] = " - " + title
		}
		if date, ok := frontmatter["date"]; ok {
			context["date"] = "<p class=\"date\">Published " + date + "</p>"
		}
		if description, ok := frontmatter["description"]; ok {
			context["description"] = "<p class=\"subtitle\">" + description + "</p>"
		}

		err = render(fileContents, "../public/"+outputFilename, context)
		if err != nil {
			panic(err)
		}
	}
}

func readTemplateFiles() (string, string, string) {
	templateBytes, err := os.ReadFile("../layout/template.html")
	if err != nil {
		panic(err)
	}
	templateStr := string(templateBytes)

	headBytes, err := os.ReadFile("../layout/head.html")
	if err != nil {
		panic(err)
	}
	headStr := string(headBytes)

	headerBytes, err := os.ReadFile("../layout/header.html")
	if err != nil {
		panic(err)
	}
	headerStr := string(headerBytes)

	return templateStr, headStr, headerStr
}

func render(content string, filename string, context map[string]string) error {
	renderedHead, err := mustache.Render(head, context)
	if err != nil {
		return err
	}
	context["head"] = renderedHead
	context["content"] = "<div class=\"content\">" + content + "</div>"
	context["header"] = header

	rendered, err := mustache.Render(template, context)
	if err != nil {
		return err
	}

	fmt.Println("writing to file ", filename)
	err = os.WriteFile(filename, []byte(rendered), 0644)
	if err != nil {
		return err
	}

	return nil
}

func getFilenamesRecursive(root string) ([]string, error) {
	files, err := os.ReadDir(root)
	if err != nil {
		return nil, err
	}

	fileList := make([]string, 0)
	for _, file := range files {
		fullFilename := root + "/" + file.Name()

		if file.IsDir() {
			// recurse & get the list of those files
			subFileList, err := getFilenamesRecursive(fullFilename)
			if err != nil {
				return nil, err
			}

			fileList = append(fileList, subFileList...)
		} else {
			fileList = append(fileList, fullFilename)
		}
	}

	return fileList, nil
}

func parseFile(filename string) (string, string, map[string]string) {
	// regex for removing links with [this syntax](http://link)
	removeLinkRegex, err := regexp.Compile(`\[(.*?)\]\(.*?\)`)
	if err != nil {
		panic(err)
	}

	convertedLines := make([]string, 0)
	rawLines := make([]string, 0)
	in_frontmatter := false
	frontmatter := make(map[string]string)

	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		if strings.HasPrefix(line, "--") {
			// -- signals start or end of frontmatter section
			in_frontmatter = !in_frontmatter
		} else if in_frontmatter {
			// parse frontmatter keys like title, date, draft status
			colon := strings.Index(line, ": ")
			key := line[:colon]
			val := line[colon+2:]
			frontmatter[key] = val
		} else if strings.HasPrefix(line, "//") {
			// lines starting with // are kept as-is
			convertedLines = append(convertedLines, line[2:])
		} else if strings.Contains(line, "{rungame}") {
			// special code {rungame} turns into "Run Game" button
			convertedLines = append(convertedLines, rungamebtnHtml)
		} else {
			// everything else is markdown converted to html
			renderedLine := markdown.ToHTML([]byte(line), nil, nil)
			convertedLines = append(convertedLines, string(renderedLine))

			// rawLines is for the preview. Remove link syntax
			rawLines = append(rawLines, removeLinkRegex.ReplaceAllString(line, "$1"))
		}
	}

	fileContents := strings.Join(convertedLines, "\n")
	rawFileContents := strings.Join(rawLines, "\n")

	return fileContents, rawFileContents, frontmatter
}
