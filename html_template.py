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

        output = ''

        output += InfineonLogoTemplate.make()

        for item in self.items:

            if self.items[item] == selected_menu_link:
                selected = "selected_main_menu_item"
            else:
                selected = ""

            output += self.html.substitute(Link=self.items[item], Item=item, Selected=selected)

        output += DropDownMenuTemplate.make()

        output += "<br /><hr>"

        return output


class DropDownMenuTemplate:
    @staticmethod
    def make():
        return '''<div class="dropdown"><span id="top-right-menu" class="dropbtn">Menu &#x2bc6</span>
        <div class="dropdown-content">
        <a href="https://de.surveymonkey.com/r/SolutionFinder" target_"blank">Share Your Feedback</a>
        <a href="https://www.infineon.com/support" target_"blank">Technical Support</a>
        <a href="about.html" target_"blank">About</a></div></div>'''


class InfineonLogoTemplate:
    @staticmethod
    def make():
        return '''<a href="http://www.infineon.com" target="_blank"><img src="assets/img/logo-desktop-en.png" alt="INFINEON" align="middle" style="width:7%;height:7%;"></a>'''

class CompleteToolTemplate:

    html = Template('''
        <!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>${Page_Title}</title>
            <script src="assets/js/jquery.min.js"></script>
        </head>
        <body>
        <div id="load-message">Loading... Wait...</div>
        <div id='body' style="display:none;">
        <link rel="stylesheet" type="text/css" href="assets/css/complete_tool_template.css">
            ${MainMenu}
            <div id="search_input"> <input type="text" id="search_text" placeholder="Find in this table" size="30">
            </div>
            ${SwitchableContent}
        <a id="download_zip_link" 
        href=https://github.com/vbasov007/Infineon_Selection_Guide/archive/master.zip>Download for offline viewing</a>
        <script type="text/javascript" src="assets/js/startup.js"></script>
        <script type="text/javascript" src="assets/js/collapsible_view.js"></script>
        <script type="text/javascript" src="assets/js/search_highlight.js"></script>
        <script type="text/javascript" src="assets/js/get_query_variable.js"></script>
        <script type="text/javascript" src="assets/js/page_state.js"></script>
        <script type="text/javascript" src="assets/js/productpageurl.js"></script>
        <script type="text/javascript" src="assets/js/getdatafromjs.js"></script>
        <script type="text/javascript" src="assets/js/product_page_redirect.js"></script>
        </div>
        </body>
        </html>
        ''')

    def __init__(self):
        self.switchable_content = SwitchableViewMaker()
        self.switchable_content.add_level_caption(0, '')
        self.switchable_content.add_level_caption(1, '')
        self.switchable_content.add_level_caption(2, '')

        self.main_menu = ''

    def add_table(self, html):
        self.switchable_content.add_table(html)

    def add_main_menu_html(self, main_menu: str):
        self.main_menu = main_menu

    def make(self):
        return self.html.substitute(
            Page_Title="Smart Product Selection Map - Infineon Technologies",
            MainMenu=self.main_menu,
            SwitchableContent=self.switchable_content.make(),
        )
