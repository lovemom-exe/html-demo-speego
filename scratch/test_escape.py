import json
import re

s = '<script>console.log("hello");</script>'
js = json.dumps({"test": s})
escaped_js = js.replace("</script>", "<\\/script>").replace("<script>", "<\\/script>")
print("Original:", js)
print("Escaped:", escaped_js)
