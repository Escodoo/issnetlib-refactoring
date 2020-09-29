# issnetlib-refactoring

## Preparando o ambiente

    mkdir projeto
    
    cd projeto
    
    hg clone http://hg.code.sf.net/p/generateds/code
    
    git clone --branch generate_python-standard-generateDS-package add https://github.com/akretion/erpbrasil.edoc.gen/

    virtualenv -p python3 .

    source ./bin/activate

    cd generateds-code

    pip install .

    cd ..
    
    python3 ~/DEV/erpbrasil.edoc.gen/src/erpbrasil/edoc/gen/download_schema.py -n issnet -v v1.00 -u https://github.com/Escodoo/edoc-gen/raw/master-escodoo-test/Manuais/Schemas.zip

    python3 ~/DEV/erpbrasil.edoc.gen/src/erpbrasil/edoc/gen/generate_python.py -n issnet -v v1.00
