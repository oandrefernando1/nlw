from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validade_and_crate(self, http_requent: HttpRequest) -> HttpResponse:
        # body = http_requent.body
        # product_code = body ["product_code"]

        # logica de regra de negocio
        print('Estou na minha view')
        print(http_requent)


        # retorno http
        return HttpResponse(status_code=200, body={"hello": "world"})
    