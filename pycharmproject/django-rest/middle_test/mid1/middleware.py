from django.utils.deprecation import MiddlewareMixin


class Md1(MiddlewareMixin):

    def process_request(self,request):
        print('Md1处理请求')

    def process_response(self,request,response):
        print('Md1返回相应')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print('Md1在执行%s视图前'%view_func.__name__)

    def process_exception(self,request,exception):
        print('Md1处理视图异常...')


