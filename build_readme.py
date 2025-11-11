from markdown_include.include import MarkdownInclude

config = {
    "base_path": "."
}

source_file = "README.md"
output_file = "COMBINED_README.md"

markdown = MarkdownInclude(config)
combined_text = markdown.read(source_file)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(combined_text)

print(f"✅ Combined markdown written to {output_file}")
