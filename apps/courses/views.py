from rest_framework.generics import ListAPIView

from .models import Curriculum
from .serializer import CurriculumSerializer


class CurriculumListView(ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
