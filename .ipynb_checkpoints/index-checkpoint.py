from app import app, server

from routes import render_page_content

from layout.sidebar.sidebar_callbacks import toggle_collapse, toggle_classname

from pages.scatter_3d.amyloid_callbacks import make_3d_scatter

# from environment.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK

if __name__ == "__main__":
    app.run(
        # jupyter_mode="external",
        # # host=APP_HOST,
        # port="8050",
        # threaded=True,
        # debug=True,
        # dev_tools_props_check=True
    )