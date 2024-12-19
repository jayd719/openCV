import os
from datetime import datetime
JS_FILES = "../js/"



def image_tag(parent, filename, src="src"):
    return (
        f'<figure class="image-item">'
        f'<img width="50%" src="../{src}/{parent}/{filename}" alt="{filename}">' 
        f'<figcaption>{parent}/{filename}</figcaption>'
        f'</figure>'
    )

def generate_page(content, title="Results"):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
    {time_stamp()}
    <div id="resultssection">
        {content}
    </div>
    
    <script src="{JS_FILES}/app.js"></script>
</body>
</html>
"""

def time_stamp():
    return f"<p id='creation-time'>{datetime.today()}</p>"
    

def process_results(src="src", output_dir="out", output_file="results.html"):
    VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
    result = f''

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
            if ".md" in output_file:
                fh.write(result)
            else:
                
                fh.write(generate_page(result))

        print(f"HTML file generated at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_results()
