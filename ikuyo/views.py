import locale

import render as render
from django.shortcuts import render
from django.views.generic import TemplateView

from api import calculateCostOfMove, getPoint
from .forms import TravelEstimateForm

# Create your views here.
from .models import LogModel

locale.setlocale(locale.LC_NUMERIC, 'ja_JP.UTF-8')
HOTEL = 8000


def TravelEstimate(request):
    if request.method == "POST":
        form = TravelEstimateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # 出発地
            start = request.POST['start']
            # 到着地
            goal = request.POST['goal']
            # 人数
            people = request.POST['people']
            # 日数
            days = request.POST['days']

            # 緯度・経度の取得
            startCoord = getPoint(start)
            goalCoord = getPoint(goal)

            # 移動にかかる費用
            fare = calculateCostOfMove(startCoord, goalCoord)

            # 宿代を足す
            charge = HOTEL * int(days) * int(people)
            fare += charge

            # todo リザルトが保存できなくてエラー
            LogModel.objects.create(result=fare)

            info = {'start': start, 'goal': goal, 'people': people, 'days': days, 'result': fare}
            return render(request, 'result.html',context=info)
    else:
        form = TravelEstimateForm()
        return render(request, 'form.html', {'form': form, 'people_range': range(1, 9), 'days_range': range(1, 7)})


class ResultEstimate(TemplateView):
    template_name = 'result.html'
