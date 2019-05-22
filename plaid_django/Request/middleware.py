from Request.models import Request

Events = {
    "/login/" : "LOGIN",
    "/logout/" : "LOGOUT",
    "/public_token/" : "PUBLIC TOKEN LINK",
    "/firewh/" : "FIRE WEBHOOK",
    "/transactions/" : "FETCH TRANSACTIONS",
    "/wh/": "WEBHOOK"
}
def LogMiddleware(get_response):
    def middleware(request):
        
        r = Request(path = request.path)
        response = get_response(request)
        r.user = request.user if request.user.is_authenticated else None
        r.event = Events[request.path] if request.path in Events else None
        r.status = response.status_code
        if "HTTP_AUTHORIZATION" in request.META:
            r.session = request.META["HTTP_AUTHORIZATION"][6:]
        elif request.path == "/login/" and response.status_code == 201:
            r.session = response.data["token"]
        r.session = r.session[::-1] if r.session else None
        
        # special case for webhook
        if request.path == "/wh/" and "s" in request.GET:
            r.session = request.GET["s"]

        if r.event: # unwanted requests are not logged, like admin page
            r.save()
        return response

    return middleware