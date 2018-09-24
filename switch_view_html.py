from string import Template


class SwitchableViewHtml:

    def __init__(self):
        self.content = list()

    html = Template('''
    <div>
        ${Buttons}
        ${Views}
    </div>''')

    button_template = Template('''
    <button  class="change-view-but" view-id="${ViewId}">${Caption}</button>''')

    selectable_content_template = Template('''
    <div class="selectable-view" view-id="${ViewId}">${SelectableContent}</div>
    ''')

    def add_selectable_content(self, view_id, caption, selectable_content):
        self.content.append(
            {'ViewId': view_id,
             'Caption': caption,
             'SelectableContent': selectable_content,
             })

    def make(self):

        buttons_html = ''
        content_html = ''
        for view in self.content:
            buttons_html += self.button_template.substitute(
                ViewId=view['ViewId'],
                Caption=view['Caption'],
            )

            content_html += self.selectable_content_template.substitute(
                ViewId=view['ViewId'],
                SelectableContent=view['SelectableContent']
            )

        return self.html.substitute(Buttons=buttons_html, Views=content_html)

