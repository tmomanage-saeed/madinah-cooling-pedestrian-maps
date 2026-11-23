# Template + madinah_data.json -> HTML (arcpy ke baghair, sirf design badalne ke liye)
import os
H = os.path.dirname(os.path.abspath(__file__))
js = open(os.path.join(H, "madinah_data.json"), encoding="utf-8").read()
t = open(os.path.join(H, "template.html"), encoding="utf-8").read()
out = os.path.join(H, "Madinah_Cooling_Pedestrian_Maps.html")
open(out, "w", encoding="utf-8").write(t.replace("/*__DATA__*/null", js))
print(out, round(os.path.getsize(out) / 1e6, 1), "MB")
