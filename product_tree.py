import pandas as pd
from validators import url as is_url
from dataframe_proc_utility import variations, take_only, annotations_with_title, get_single_col_value, count_rows
from html_format_utility import span_format, format_multiline_annot, format_val_with_measure_units_html


def table_to_tree(
        df, tree_level_names, parent_node,
        last_level_annotations,
        pop_up_notes,
        last_level_url_col_name=None,
        ):

    if df.empty:
        return

    line_break = '<br />'

    conditions = variations(df, tree_level_names[0])
    for c in conditions:
        if pd.isna(c):
            continue

        filtered_df = take_only(df, tree_level_names[0], c)

        flag_new_product = False
        if count_rows(filtered_df, 'new_product', 'new'):
            flag_new_product = True

        c = format_val_with_measure_units_html(c)
        c = span_format(tree_level_names[0], c)

        if len(tree_level_names) > 1:
            new_node = parent_node.new_node(c, parent_node)
            new_node.set_flag_new(flag_new_product)

            table_to_tree(
                filtered_df,
                tree_level_names[1:],
                new_node,
                last_level_annotations,
                pop_up_notes,
                last_level_url_col_name=last_level_url_col_name,)
        else:
            ann_list = annotations_with_title(filtered_df, last_level_annotations)
            pop_up_notes_list = annotations_with_title(filtered_df, pop_up_notes)

            ann_list.extend(pop_up_notes_list)

            new_node = parent_node.new_node(
                "{0}{1}{2}".format(c, line_break, format_multiline_annot(ann_list)), parent_node)

            if last_level_url_col_name:
                url = get_single_col_value(filtered_df, last_level_url_col_name)
                if is_url(url):
                    new_node.set_url(url)

            new_node.set_flag_new(flag_new_product)

    return


def parameter_names_tree(tree_level_names, attach_to_node):
    prev_node = attach_to_node
    for level in tree_level_names:
        new_node = attach_to_node.new_node('{0}'.format(level), parent=prev_node)
        prev_node = new_node
