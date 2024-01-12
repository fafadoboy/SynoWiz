#!/bin/bash

# generate practice server
java -jar ${PERSONAL_TOOLS_DIR}/swagger-codegen-cli-2.2.1.jar generate -l python-flask -i ../server/practice/swagger/swagger.json -o ../server/practice/

# generate practice client
java -jar ${PERSONAL_TOOLS_DIR}/swagger-codegen-cli-2.2.1.jar generate -l python -i ../server/practice/swagger/swagger.json -o ../client/practice/


# generate lexico server
java -jar ${PERSONAL_TOOLS_DIR}/swagger-codegen-cli-2.2.1.jar generate -l python-flask -i ../server/lexico/swagger/swagger.json -o ../server/lexico/

# generate lexico client
java -jar ${PERSONAL_TOOLS_DIR}/swagger-codegen-cli-2.2.1.jar generate -l python -i ../server/lexico/swagger/swagger.json -o ../client/lexico/
