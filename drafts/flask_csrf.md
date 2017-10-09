Title: template
Slug: template
Date: 2017-09-15 19:49
Category: Python
Tags: pelican, blog, xaled
Author: Khalid Grandi
Summary: Template

A simple CSRF protection for Flask

What is CSRF

OWAS CSRF Protection
* unique token
* checking referrer
* checking session

I've implemented a module in kutils that does tthis

import kutils.flaskutils as fu+
csrf_token = fu.get_csrf_token(form_id="form1")
print fu.check_csrf_token(csrf_token)

csrf_token = fu.get_csrf_token(form_id="form2", referer="page1", session_id="user1")
print fu.check_csrf_token(csrf_token, form_id="form1", referer="page1", session_id="user1")


Flask wrapper
like cache wrapper in the flask documentation: url

----------------------------
def csrf_error():
    return Response('Bad request.', 401)

def requires_csrf_check(form_id=None, token_name="_csrf_token", unvalidate=True):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            session_id = get_session_id()
            referer = request.referrer
            token = request.form[token_name]
            logger.debug("checking csrf token: token=%s, form_id=%s, referrer=%s, session_id=%s", token, form_id, referer, session_id)
            if not check_csrf_token(token, form_id=form_id , referer=referer, session_id=session_id, unvalidate=unvalidate):
                return csrf_error()
            return f(*args, **kwargs)
        return decorated
    return decorator

----------------------------
    

@app.route('/origin')
def origin():
    csrftoken = get_csrf_token(form_id="form1", referer=request.url, session_id=get_session_id())
    return """<html><body><form action="/destination" method="POST"><input type="hidden" name="_csrf_token" value="%s" /><input type="submit" value="submit" /></form></body></html> """%csrftoken


@app.route('/destination',methods=['POST'])
@requires_csrf_check(form_id="form1")
def destination():
    return "success"
    
    
    
