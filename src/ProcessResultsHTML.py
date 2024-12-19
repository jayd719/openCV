import os
from datetime import datetime

JS_FILES = "../js/"


def image_tag(parent, filename, src="src"):
    """Generate an HTML image tag with a caption."""
    return (
        f'<figure class="image-item">'
        f'<img width="50%" src="../{src}/{parent}/{filename}" alt="{filename}">'
        f'<figcaption>{parent}/{filename}</figcaption>'
        f'</figure>'
    )


def generate_page(content, title="Results"):
    """Generate a complete HTML page."""
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Image results page">
    <title>{title}</title>
</head>
<body>
    {time_stamp()}
    <div id="resultssection">
        {content}
    </div>
    <script src="{os.path.join(JS_FILES, 'app.js')}"></script>
</body>
</html>
"""


def time_stamp():
    """Generate a timestamp for the HTML."""
    return f"<p id='creation-time'>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"


def process_results(src="src", output_dir="out", output_file="results.html"):
    """Process image directories and generate an HTML file."""
    VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
    result = ""

    try:
        for section in os.listdir(src):
            section_path = os.path.join(src, section)
            if not os.path.isdir(section_path):
                continue

            result += f"<div class='image-grid'><h3>{section}</h3><br>"

            for image in sorted(os.listdir(section_path)):
                if os.path.splitext(image)[1].lower() not in VALID_EXTENSIONS:
                    continue
                result += image_tag(section, image, src)

            result += "</div>"

        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, output_file)

        with open(output_path, 'w', encoding="utf-8") as fh:
            if output_file.endswith(".md"):
                fh.write(result)
            else:
                fh.write(generate_page(result))

        print(f"HTML file generated at: {output_path}")
    except Exception as e:
        print(f"Error while processing results: {e}")


if __name__ == "__main__":
    process_results()
