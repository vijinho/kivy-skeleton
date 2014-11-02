RELEASE=$1
ALIAS=skeleton
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ~/.keystores/${ALIAS}.keystore ~/vagrant/PocketPhilosopher-$1-release-unsigned.apk ${ALIAS}
/Applications/Android-sdk//build-tools/android-4.4W/zipalign  -v 4 ~/vagrant/PocketPhilosopher-$1-release-unsigned.apk ~/vagrant/PocketPhilosopher-$1-release-signed.apk
