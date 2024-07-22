from dash import Dash,html
from dash_bootstrap_components.themes import BOOTSTRAP
from component.layout import create_layout
def main() :
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Rongrean dashboard"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__" :
    main()