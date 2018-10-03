"""
Usage: build_tool CONFIG_XLSX [--in_folder=INPUT_FOLDER] [--out_folder=OUTPUT_FOLDER] [-p]
                    [--row=CONFIG_FILE_ROW]...

Arguments:
    CONFIG_XLSX         Config excel file path
    INPUT_FOLDER        Input data folder
    OUTPUT_FOLDER       Output data folder

Options:
    -h --help
    -i --in_folder=INPUT_FOLDER
    -o --out_folder=OUTPUT_FOLDER
    -r --row=CONFIG_FILE_ROW
    -p --print                          Print more information

"""

from docopt import docopt
import pandas as pd
import os
from html_template import CompleteToolTemplate
from product_table_to_html import product_table_to_html
from printing_utility import print_header_value_variation_stat


def build_tool():

    args = docopt(__doc__)

    print(args)

    input_folder = ''
    if args['--in_folder']:
        input_folder = args['--in_folder']

    output_folder = ''
    if args['--out_folder']:
        output_folder = args['--out_folder']

    config_df = pd.read_excel(os.path.join(input_folder, args['CONFIG_XLSX']))

    config_df.fillna('', inplace=True)

    config_df.set_index('index')

    config_dict = config_df.to_dict('index')

    print(list(config_dict))

    if args['--row']:
        row_index_list = list(map(int, args['--row']))
    else:
        row_index_list = list(map(int, list(config_dict)))

    print(row_index_list)

    output_files_dict = dict()
    for i in row_index_list:
        row = config_dict[i]
        output_file_name = row['output_html']
        if output_file_name not in output_files_dict:
            output_files_dict.update({output_file_name: CompleteToolTemplate()})


    for i in row_index_list:
        row = config_dict[i]
        row = {str(key): str(row[key]) for key in row}
        df = pd.read_excel(os.path.join(input_folder, row['input_xlsx']))

        if args['--print']:
            print(row)
            print_header_value_variation_stat(df)

        table_html = product_table_to_html(
            df,
            row['category'],
            row['subcategory'],
            row['view'],
            row['main_topic'],
            row['tree'],
            row['attributes'],
            row['url_source'],
            row['exclude'],
            row['include_only'],
            row['match'],
            )
        template = output_files_dict[row['output_html']]
        template.add_table(table_html)

    for file_name in output_files_dict:
        out_html = output_files_dict[file_name].make()
        with open(os.path.join(output_folder, file_name), "w", encoding='utf-8') as out_html_file:
            out_html_file.write(out_html)


def build_tool_test():

    file_list = ["f1.html", "f2.html", "f3.html"]

    template = CompleteToolTemplate()

    for file_name in file_list:
        with open(file_name, "r", encoding='utf-8') as html_file:
            html = html_file.read()
        template.add_table(html)

    out_html = template.make()

    with open("out.html", "w", encoding='utf-8') as out_html_file:
        out_html_file.write(out_html)


if __name__ == '__main__':
    build_tool()
