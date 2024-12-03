const ua = navigator.userAgent.toLowerCase();
let device = "Desktop"

if (/tablet|ipad/i.test(ua)) {
    device = "Tablet";
} else if (/mobi|android|iphone|ipod/i.test(ua)) {
    device = "Smartphone";
}

liveSend(
    {
        'type': 'device',
        'device': device
    }
)
