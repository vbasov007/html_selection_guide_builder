from anytree import Node
import copy
from html_parser import get_div_tag_attributes

from switch_view_html import SwitchableViewHtml

class SwitchableViewMaker:

    def __init__(self):
        self.content_tree_root = Node('root')
        self.switchable_view = SwitchableViewHtml()
        pass

    def _build_content_tree(self, main_category_name, sub_category_name, view_name, table_html):

        def update_tree(node_name, parent):
            for node in parent.children:
                if node.name == node_name:
                    return node
            return Node(node_name, parent=parent)

        def add_data(node, data):
            #node.__dict__.update({"table_html": copy.deepcopy(data)})
            node.__dict__.update({"table_html": data})

        level = update_tree(main_category_name, self.content_tree_root)
        level = update_tree(sub_category_name, level)
        level = update_tree(view_name, level)
        add_data(level, table_html)

    def add_table(self, table_html):

        attr = get_div_tag_attributes(table_html)

        self._build_content_tree(
            attr['data-main-category'],
            attr['data-subcategory'],
            attr['data-view-name'],
            table_html,)

    def make(self):
        def make_level(root_node):
            svh = SwitchableViewHtml()

            if len(root_node.children) > 0:
                for n in root_node.children:
                    svh.add_selectable_content(n.name, n.name, make_level(n))
                return svh.make()
            else:
                if "table_html" in root_node.__dict__:
                    return root_node.__dict__['table_html']
                else:
                    return "NO DATA"

        return make_level(self.content_tree_root)

