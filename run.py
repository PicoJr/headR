import json
import argparse

from collections import namedtuple
from typing import List, Tuple

from jinja2 import Template

# start (bit), end (bit)
Field = namedtuple("Field", "name start end")

# size (bit)
Cell = namedtuple("Cell", "name size")

Row = namedtuple("Row", "octet bit cells")


def parse_json(json_path) -> Tuple[int, List[Field]]:
    with open(json_path) as json_data:
        data = json.load(json_data)
        bytes_per_line = data["bytes"]
        fields = []
        for field in data["fields"]:
            fields.append(Field(field["name"], field["start"], field["end"]))
        return bytes_per_line, fields


def take_at_most(fields, bits):
    total = 0
    fields_used = []
    fields_remaining = []
    for field in fields:
        size = field.end - field.start + 1
        left = bits - total
        used = min(size, left)
        if 0 < used < size:
            fields_used.append(Field(field.name, field.start, field.end - used))
            fields_remaining.append(Field(field.name, field.start + used, field.end))
        elif used == size:
            fields_used.append(field)
        else:
            fields_remaining.append(field)
        total += used
    return fields_used, fields_remaining


def rows(content: List[Field], bytes_per_line) -> Row:
    remaining = content
    octet = 0
    while remaining:
        fields_used, fields_remaining = take_at_most(remaining, bytes_per_line * 8)
        cells = []
        for field in fields_used:
            size = field.end - field.start + 1
            cells.append(Cell(field.name, size))
        yield Row(octet, octet * 8, cells)
        octet += bytes_per_line
        remaining = fields_remaining


def main():
    parser = argparse.ArgumentParser(description="json header description to html")
    parser.add_argument("json", help="json path")
    parser.add_argument("--out", default="out.html", help="output path for html file")
    args = parser.parse_args()

    bytes_per_line, fields = parse_json(args.json)
    bytes_numbering = list(range(bytes_per_line))
    bits_numbering = list(range(bytes_per_line * 8))
    with open("templates/template.html") as file_:
        template = Template(file_.read())
        result = template.render(
            bytes_numbering=bytes_numbering,
            bits_numbering=bits_numbering,
            rows=list(rows(fields, bytes_per_line)),
        )
    with open(args.out, "w+") as out_html:
        out_html.write(result)


if __name__ == "__main__":
    main()
