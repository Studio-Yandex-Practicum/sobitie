import asyncio

from channels.layers import get_channel_layer
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(http_method_names=['POST'])
def send_event_notification(request):
    """Принимает запрос на отправку уведомлений и обрабатывает его."""
    if request.method == 'POST':
        try:
            event_data = request.POST.dict()
            channel_layer = get_channel_layer()
            asyncio.run(channel_layer.send("send_event_notification", {"type": "send_event", "text": event_data}))
            return JsonResponse({"message": "Отправка уведомлений началась."})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': "Разрешён только метод POST."}, status=405)
