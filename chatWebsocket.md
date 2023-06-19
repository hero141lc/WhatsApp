curl 'wss://web.whatsapp.com/ws/chat' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0' -H 'Accept: */*' -H 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' -H 'Accept-Encoding: gzip, deflate, br' -H 'Sec-WebSocket-Version: 13' -H 'Origin: https://web.whatsapp.com' -H 'Sec-WebSocket-Extensions: permessage-deflate' -H 'Sec-WebSocket-Key: ue6KZBf07RMcvSC/61UcHw==' -H 'Connection: keep-alive, Upgrade' -H 'Sec-Fetch-Dest: websocket' -H 'Sec-Fetch-Mode: websocket' -H 'Sec-Fetch-Site: same-origin' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Upgrade: websocket'

await fetch("wss://web.whatsapp.com/ws/chat", {
    "credentials": "omit",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Sec-WebSocket-Version": "13",
        "Sec-WebSocket-Extensions": "permessage-deflate",
        "Sec-WebSocket-Key": "ue6KZBf07RMcvSC/61UcHw==",
        "Sec-Fetch-Dest": "websocket",
        "Sec-Fetch-Mode": "websocket",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    },
    "method": "GET",
    "mode": "cors"
});
