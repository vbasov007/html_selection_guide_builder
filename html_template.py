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


class MainMenuTemplate:

    html = Template('''<a href="${Link}" class="main-menu-but ${Selected}">${Item}</a>''')

    def __init__(self):
        self.items = dict()

    def add_item(self, item, link):
        self.items.update({item: link})

    def make(self, selected_menu_link=None):

        output = '''
            <a id="download_zip_link"
            href=https://github.com/vbasov007/Infineon_Selection_Guide/archive/master.zip>
                DOWNLOAD FOR OFFLINE VIEWING
            </a><br /><br />'''
        for item in self.items:

            if self.items[item] == selected_menu_link:
                selected = "selected_main_menu_item"
            else:
                selected = ""

            output += self.html.substitute(Link=self.items[item], Item=item, Selected=selected)
        output += "<br /><hr>"

        return output


class CompleteToolTemplate:

    html = Template('''
        <!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>${Page_Title}</title>
            <script src="assets/js/jquery.min.js"></script>
        </head>
        <link rel="stylesheet" type="text/css" href="assets/css/complete_tool_template.css">
            ${MainMenu}
            <div id="search_input">
            HIGHLIGHT KEYWORD: <input type="text" id="search_text" placeholder="Type word and press Enter" size="30">
            </div>
            ${SwitchableContent}
        <script type="text/javascript" src="assets/js/complete_tool_template.js"></script>
        <script type="text/javascript" src="assets/js/search_highlight.js"></script>
        <body>
        </body>
        </html>
        ''')

    def __init__(self):
        self.switchable_content = SwitchableViewMaker()
        self.switchable_content.add_level_caption(0, 'CATEGORY: ')
        self.switchable_content.add_level_caption(1, 'SUB-CATEGORY: ')
        self.switchable_content.add_level_caption(2, 'SELECT PART BY: ')

        self.main_menu = ''

    def add_table(self, html):
        self.switchable_content.add_table(html)

    def add_main_menu_html(self, main_menu: str):
        self.main_menu = main_menu

    def make(self):
        return self.html.substitute(
            Page_Title="Product Selection Tool",
            MainMenu=self.main_menu,
            SwitchableContent=self.switchable_content.make(),
        )
