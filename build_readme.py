import re
from pathlib import Path

def process_includes(file_path, base_path="."):
    content = Path(file_path).read_text(encoding="utf-8")
    include_pattern = re.compile(r'#include\s+"([^"]+)"')

    def include_replacer(match):
        include_file = Path(base_path) / match.group(1)
        if include_file.exists():
            print(f"Including: {include_file}")
            return include_file.read_text(encoding="utf-8")
        else:
            print(f"⚠️ File not found: {include_file}")
            return f"<!-- Missing include: {match.group(1)} -->"

    # Replace all include directives recursively
    while include_pattern.search(content):
        content = include_pattern.sub(include_replacer, content)

    return content


if __name__ == "__main__":
    source_file = "README_BASE.md"
    output_file = "README.md"

    combined = process_includes(source_file, base_path=".")
    Path(output_file).write_text(combined, encoding="utf-8")

    print(f"\n✅ Combined markdown written to {output_file}")
