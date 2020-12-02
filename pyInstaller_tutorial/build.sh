source bin/activate
pyinstaller src/wsgi.py -F \
--name "dsc-os-linux" \
--add-data "src/data/*:data" \
--add-data "src/data/*.jpeg:data" \
--hidden-import waitress\
--clean
