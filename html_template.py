from string import Template
from html_page_content import SwitchableViewMaker


class ProductTableOnly:

    html = Template('''
    <div 
        data-main-category="${Category}"
        data-subcategory="${Subcategory}"
        data-view-name="${View_Name}">
     <table>
        <tr>
        ${Table_Headers}
        </tr>
        <tr>
        ${Table_Content}
        </tr>
    </table>
    </div>
    ''')

    def make(self, **f):
        return self.html.substitute(
            Category=f['Category'],
            Subcategory=f['Subcategory'],
            View_Name=f['View_Name'],
            Page_Title=f['Page_Title'],
            Table_Title=f['Table_Title'],
            Table_Headers=f['Table_Headers'],
            Table_Content=f['Table_Content'],
        )


class CompleteToolTemplate:

    html = Template('''
        <!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>${Page_Title}</title>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        </head>
        <link rel="stylesheet" type="text/css" href="assets/css/complete_tool_template.css">
            ${SwitchableContent}
        <script type="text/javascript" src="assets/js/complete_tool_template.js"></script>
        <body>
        </body>
        </html>
        ''')

    def __init__(self):
        self.switchable_content = SwitchableViewMaker()
        self.switchable_content.add_level_caption(0, 'CATEGORY: ')
        self.switchable_content.add_level_caption(1, 'SUB-CATEGORY: ')
        self.switchable_content.add_level_caption(2, 'SELECT PART BY: ')

    def add_table(self, html):
        self.switchable_content.add_table(html)

    def make(self):
        return self.html.substitute(
            Page_Title="Product Selection Tool",
            SwitchableContent=self.switchable_content.make(),
        )
