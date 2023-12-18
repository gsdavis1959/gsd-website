mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"gregory_s_davis@yahoo.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
\n\
[theme]\n\
primaryColor = '#eb4034'\n\
backgroundColor = '#021d24'\n\
secondaryBackgroundColor = '#B9F1C0'\n\
textColor = '#FFFFFF'\n\
font = 'sans serif'\n\
" > ~/.streamlit/config.toml