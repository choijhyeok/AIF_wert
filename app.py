import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="HashTrip",initial_sidebar_state="collapsed",layout="wide")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


CDN_PATH = 'https://cdn.knightlab.com/libs/timeline3/latest'
CSS_PATH = 'timeline3/css/timeline.css'
JS_PATH = 'timeline3/js/timeline.js'

SOURCE_TYPE = 'json' # json or gdocs
JSON_PATH = 'timeline_setting.json' # example json
TL_HEIGHT = 640 # px


# load data
json_text = ''
if SOURCE_TYPE == 'json':
    with open(JSON_PATH, "r") as f:
        json_text = f.read()
        source_param = 'timeline_json'
        source_block = f'var {source_param} = {json_text};'



# load css + js
css_block = f'<link title="timeline-styles" rel="stylesheet" href="{CDN_PATH}/css/timeline.css">'
js_block  = f'<script src="{CDN_PATH}/js/timeline.js"></script>'


# write html block
htmlcode = css_block + ''' 
''' + js_block + '''

    <div id='timeline-embed' style="width: 100%; height: '''+str(TL_HEIGHT)+'''px; margin: 1px;"></div>

    <script type="text/javascript">
        var additionalOptions = {
            start_at_end: false, is_embed:true,
        }
        '''+source_block+'''
        timeline = new TL.Timeline('timeline-embed', '''+source_param+''', additionalOptions);
    </script>'''


#UI sections
data = 'Data'
code = 'HTML Code'
line = 'Visualization'
about = 'About'

components.html(htmlcode, height=TL_HEIGHT,)



        

    