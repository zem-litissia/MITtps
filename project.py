import csv

def read_text_to_dict(txt_file):
    """
    Reads tab-separated data from a text file and converts it into a list of dictionaries.
    Each line corresponds to one record with tab-separated fields.
    """
    data = []
    with open(txt_file, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            data.append(row)
    return data


def data_to_html(data):
    """
    Converts the list of dictionaries into an HTML table.
    """
    html = ['<html><head><meta charset="utf-8"><title>Text File Output</title>',
            '<style>',
            'table {border-collapse: collapse; width: 100%;}',
            'th, td {border: 1px solid #666; padding: 8px; text-align: left;}',
            'th {background-color: #f2f2f2;}',
            'body {font-family: Arial, sans-serif; margin: 20px;}',
            '</style></head><body>']

    html.append("<h1>Projet de tp01 MIT -Zemmour litissia , Tahraoui bochra-</h1>")
    html.append("<h2>Data from Text File</h2>")
    if not data:
        html.append("<p>No data found.</p>")
    else:
        # Create table header from keys
        html.append("<table>")
        html.append("<tr>" + "".join([f"<th>{key}</th>" for key in data[0].keys()]) + "</tr>")

        # Add table rows
        for row in data:
            html.append("<tr>" + "".join([f"<td>{value}</td>" for value in row.values()]) + "</tr>")
        html.append("</table>")

    html.append("</body></html>")
    return "\n".join(html)


# --------- TEST ---------
if __name__ == "__main__":
    filename = "members.txt"

    result = read_text_to_dict(filename)
    print(result)  # Display in console for verification

    html_content = data_to_html(result)
    output_file = "members.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML file generated successfully: {output_file}")
