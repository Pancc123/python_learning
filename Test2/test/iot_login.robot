*** Settings ***
Library           RequestsLibrary
Library           requests

*** Variables ***
${url}            https://iot.smarteoc.com/api/latest/user/serviceProviderLogin
${username}       pcc
${password}       pan123

*** Test Cases ***
login_ok
    ${header}    CreateDictionary    Content-Type=application/json    Connection=keep-alive
    ${postdata}    CreateDictionary    action=serviceProviderLogin    username=${username}    password=${password}    exp=1
    ${req}    Post    ${url}    json=${postdata}    headers=${header}
    log    ${req.content}
    ${a}    Set variable    ok
    log    ${a}
    log    ${req.content.decode("utf-8")}
