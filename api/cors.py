from django.middleware.common import CommonMiddleware
class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

class CORSMiddleware(MiddlewareMixin):
    def process_response(self,request,response):
        # 在中间件中设置url拦截为任意能获取
        response['Access-Control-Allow-Origin'] = '*'

        if request.method == "OPTIONS":
            response['Access-Control-Allow-Headers'] = "Content-Type"

        return response