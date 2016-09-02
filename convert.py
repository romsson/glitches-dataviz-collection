# -*- coding: utf-8 -*-
import json

def open_json(filename):
    with open(filename, "r") as fp:
        data = json.load(fp)
        return data;
        
def convert_json_table(json, filename):

    table = open(filename, "w")
    table.write("<html>\n\t<body>\n\t\t<table>\n")
    for j in json:
        table.write("\t\t\t<tr><td><a href='images/%s'><img src='images/%s' style='width:200px'></a></td><td><a href='%s'>%s</a></td></tr>\n" % (j['filename'], j['filename'], j['post_url'], j['text']))
        
    table.write("\t\t</table>\t\n</body>\n</html>\n")
    table.close()
        
if __name__ == "__main__":
    collection = open_json("glitches.json")
    convert_json_table(collection, "table.html")
