import excel
import htmlmin

html = excel.get_all_the_rows_from_column('B')
html_code_rows = []

for i in range(1, len(html)):
    minimized_html = htmlmin.minify(html[i], remove_empty_space = True)
    html_code_rows.append(minimized_html)
    print(minimized_html)

excel.write_html_to_excel(html_code_rows, 'C')
