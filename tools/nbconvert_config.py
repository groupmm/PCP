# nbconvert config file for embedding png files in html files

import base64, os, re
from nbconvert.preprocessors import Preprocessor

class InlineImagesPreprocessor(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        if cell.cell_type == "markdown" and "<img" in cell.source:
            # Find src="...png" or src="...svg"
            mime_map = {".png": "image/png", ".svg": "image/svg+xml"}
            matches = re.findall(r'src="([^"]+\.(?:png|svg))"', cell.source)
            for path in matches:
                if os.path.exists(path):
                    ext = os.path.splitext(path)[1].lower()
                    mime = mime_map[ext]
                    with open(path, "rb") as f:
                        b64 = base64.b64encode(f.read()).decode("utf-8")
                    cell.source = cell.source.replace(
                        f'src="{path}"',
                        f'src="data:{mime};base64,{b64}"'
                    )
        return cell, resources
    
# Register the preprocessor
c = get_config()
c.Exporter.preprocessors = [InlineImagesPreprocessor]
