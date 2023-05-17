#!/bin/bash

output_path=Editor_ui.py
input_path=editor.ui

pyuic6 -o $output_path -x $input_path
python .\edit_ui_file.py
echo "Output saved to $output_path"
