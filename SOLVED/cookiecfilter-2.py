#soluzione: http://cookie.challs.olicyber.it/
#vai sul sito http://cookie.challs.olicyber.it/
#apri la console
# esegui  il seguente codice javascript in console
#counter=199999999999999
#premi il biscotto
import base64
flag = "SVRBU0VDezk5OTk5OTk5OTk5OTk5XzE3NV80X2wxNzdsM183MDBfbXVjaF9kMG43X3kwdV83aDFuaz99";
decoded=base64.b64decode(flag)
print(decoded)
