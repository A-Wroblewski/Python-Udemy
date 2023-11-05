import qdarktheme

qss = '''
QPushButton[cssClass="specialButton"] {
    color: #fff;
    background: '#1e81b0';
}

QPushButton[cssClass="specialButton"]:hover {
    background: '#16658a';
}

QPushButton[cssClass="specialButton"]:pressed {
    background: '#115270';
}
'''

def config_style():
    qdarktheme.setup_theme(
        theme='auto',
        custom_colors={'primary': '#1e81b0'},
        additional_qss=qss,
    )
