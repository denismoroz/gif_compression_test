import os

gif_compress = "./gifsicle"


os.chdir("./")


params = "-O3 --lossy=80 -o %s %s"
input_dir = "./input"
output_dir = "./output"

processed_files = []

for f in os.listdir(input_dir):
    input_f = os.path.join(input_dir, f)
    output_f = os.path.join(output_dir, f)
    cmd = "%s %s" %(gif_compress, params % (output_f, input_f))
    os.system(cmd)

    input_file_size = os.path.getsize(input_f)
    output_file_size = os.path.getsize(output_f)

    result = 100.0 - float(output_file_size)/float(input_file_size) * 100

    processed_files.append((input_f, input_file_size, output_f, output_file_size, result))


html_tpl_begin = "<!DOCTYPE html><html><head></head><body>"
html_tpl_end = "</body></html>"

resulting_html = html_tpl_begin
for r in processed_files:
    resulting_html += "<div>"
    resulting_html +=   '<img src="%s"/>' % r[0]
    resulting_html +=   '<h3> Size: ' + str(r[1]/(1024*1024.0)) + ' MB</h3>'
    resulting_html +=   '<img src="%s"/>' % r[2]
    resulting_html += '<h3> Size: ' + str(r[3]/(1024*1024.0)) + ' MB</h3>'
    resulting_html += '<h1> Compression: - ' + str(r[4]) + '%</h1>'
    resulting_html += "</div>"

resulting_html += html_tpl_end

with open("./index.html", "w") as f:
    f.write(resulting_html)

print("\n".join([str(r) for r in processed_files]))


