mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"gregory_s_davis@yahoo.com\"\n\
" > ~/.streamlit/credentials.toml

echo "[server]"
echo "headless = true"
echo "port = $PORT"
echo "enableCORS = false"