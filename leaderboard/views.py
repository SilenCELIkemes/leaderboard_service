from rest_framework.views import APIView
import logging
from django.http.response import JsonResponse
from models import Score
import json
logger = logging.getLogger('django')


class ScoreView(APIView):

    def get(self, request, **kwargs):
        return 'welcome'

    def post(self, request, **kwargs):
        data = request.data.get('params')
        if isinstance(data, unicode):
            data = json.loads(data.decode('utf8'))
        params = data.get('params')

        logger.info(u'===CLASS:{0}===REQUEST.DATA:{1}==='.format(self.__class__.__name__,
                                                                                json.dumps(params)))

        try:
            c_id = params.get('c_id')
            c_score = params.get('c_score')
            if not isinstance(c_id, int) or not isinstance(c_score, int):
                return JsonResponse({"status": False, "error_message": 'ID OR SCORE IS NOT INT'})
            if c_score > 10000000 or c_score < 1:
                return JsonResponse({"status": False, "error_message": 'SCORE IS NOT BETWEEN 1 AND 10000000'})
            affect = Score.objects.create(customer_id=c_id, score=c_score)
            logger.info('CREATE_RESULT:{0},c_id:{1},c_score:{2}'.format(affect, c_id, c_score))
            return JsonResponse({"status": True, "error_message": 'SUCCESSFUL'})
        except Exception as e:
            logger.exception(e)
            return JsonResponse({"status": False, "error_message": e})

class SearchView(APIView):

    def post(self, request, **kwargs):
        data = request.data.get('params')
        if isinstance(data, unicode):
            data = json.loads(data.decode('utf8'))
        params = data.get('params')

        logger.info(u'===CLASS:{0}===REQUEST.DATA:{1}==='.format(self.__class__.__name__,
                                                                                json.dumps(params)))

        try:
            begin_point = params.get('begin_point')
            end_point = params.get('end_point')
            customer_id = params.get('c_id')
            if not isinstance(begin_point, int) or not isinstance(end_point, int):
                return JsonResponse({"status": False, "error_message": 'POINT IS NOT INT'})
            result = Score.objects.order_by("-score")[begin_point - 1: end_point - 1]
            logger.info('RESUlT:{0}'.format(result))
            return_data = []
            for i in result:
                d = {}
                d['c_id'] = i.customer_id
                d['c_score'] = i.score
                return_data.append(d)
            extend_data = Score.objects.filter(customer_id=customer_id).first()
            print (customer_id, extend_data.score)
            return_data.append({"c_id": customer_id, "c_score": extend_data.score})
            return JsonResponse({"status": True, "dara": return_data})
        except Exception as e:
            logger.exception(e)
            return JsonResponse({"status": False, "error_message": e})
