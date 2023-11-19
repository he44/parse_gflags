import argparse
import json
import os
from xml.etree import ElementTree


def parse_flag_xml_to_json(xml_content):
    root = ElementTree.fromstring(xml_content)

    # Extract data.
    data = {
        "program": root.find("program").text,
        "usage": root.find("usage").text,
        "flags": []
    }

    # Iterate over each flag.
    for flag in root.findall("flag"):
        flag_data = {child.tag: child.text for child in flag}
        # Only keep the flags that are specified in the current directory.
        if not flag_data["file"].startswith("/Users/"):
            continue
        # Keep the file name only.
        flag_data["file"] = flag_data["file"].split("/")[-1]
        data["flags"].append(flag_data)

    return data


def main():
    parser = argparse.ArgumentParser(description='Parse flag XML to JSON')
    parser.add_argument('--input_file', '-i', type=str,
                        help='Path to the input XML file')
    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        raise ValueError(
            'Input file does not exist at path: {}'.format(args.input_file))

    # Read XML content from input file.
    with open(args.input_file, 'r') as file:
        xml_content = file.read()

    # Parse XML to JSON.
    json_data = parse_flag_xml_to_json(xml_content)
    print(f"Parsed {len(json_data['flags'])} flags")

    # Writes json data to a file.
    with open("flags.json", "w") as outfile:
        json.dump(json_data, outfile, indent=4)


if __name__ == '__main__':
    main()
