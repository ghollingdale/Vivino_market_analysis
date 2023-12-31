import streamlit as st
import streamlit.components.v1 as components

st.markdown(
    """
<style>
    .block-container {
      max-width: 100%;
    }
</style>
""",
    unsafe_allow_html=True,
)


components.html(
    """
<div class='tableauPlaceholder' id='viz1693561505000' style='position: relative'><noscript><a href='#'><img alt='Vivino: A Tableau Story ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;Vivino_visualisations_gh&#47;VivinoATableaustory&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Vivino_visualisations_gh&#47;VivinoATableaustory' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;Vivino_visualisations_gh&#47;VivinoATableaustory&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1693561505000');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
  """, width=1150, height=900
)
