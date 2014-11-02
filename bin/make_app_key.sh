cd ~
mkdir -p .keystores
ALIAS=skeleton
keytool -genkey -v -keystore ~/.keystores/${ALIAS}.keystore -alias ${ALIAS} -keyalg RSA -keysize 2048 -validity 10000
